from flask import Flask, render_template, request, jsonify
import numpy as np
from fractions import Fraction
import json

app = Flask(__name__)

class MarkovChain:
    def __init__(self, transition_matrix):
        self.P = np.array(transition_matrix, dtype=float)
        self.n_states = len(transition_matrix)
        self.steps = []
        
    def validate_matrix(self):
        """Valida que la matriz sea estocástica"""
        row_sums = np.sum(self.P, axis=1)
        return np.allclose(row_sums, 1.0)
    
    def calculate_steady_state(self):
        """Calcula el estado estacionario paso a paso"""
        self.steps = []
        
        # Paso 1: Verificar matriz estocástica
        if not self.validate_matrix():
            return {"error": "La matriz no es estocástica (las filas no suman 1)"}
        
        self.steps.append({
            "step": 1,
            "title": "Verificación de Matriz Estocástica",
            "description": "Verificamos que cada fila sume 1",
            "matrix": self.P.tolist(),
            "row_sums": np.sum(self.P, axis=1).tolist(),
            "valid": bool(True)
        })
        
        # Paso 2: Configurar sistema de ecuaciones π = πP
        # Esto es equivalente a (P^T - I)π = 0
        A = self.P.T - np.eye(self.n_states)
        
        self.steps.append({
            "step": 2,
            "title": "Sistema de Ecuaciones π = πP",
            "description": "Configuramos el sistema (P^T - I)π = 0",
            "matrix_PT": self.P.T.tolist(),
            "matrix_A": A.tolist(),
            "equation": "π = πP, donde π es el vector de estado estacionario"
        })
        
        # Paso 3: Resolver usando la condición de normalización
        # Reemplazamos la última ecuación con Σπᵢ = 1
        A_modified = A.copy()
        A_modified[-1] = np.ones(self.n_states)
        b = np.zeros(self.n_states)
        b[-1] = 1
        
        self.steps.append({
            "step": 3,
            "title": "Aplicar Condición de Normalización",
            "description": "Reemplazamos la última ecuación con Σπᵢ = 1",
            "matrix_modified": A_modified.tolist(),
            "vector_b": b.tolist()
        })
        
        # Paso 4: Resolver el sistema
        try:
            steady_state = np.linalg.solve(A_modified, b)
            
            self.steps.append({
                "step": 4,
                "title": "Solución del Sistema",
                "description": "Resolvemos el sistema de ecuaciones lineales",
                "steady_state": steady_state.tolist(),
                "steady_state_fractions": [str(Fraction(x).limit_denominator(1000)) for x in steady_state]
            })
            
            # Paso 5: Verificación
            verification = np.dot(steady_state, self.P)
            error = np.linalg.norm(verification - steady_state)
            
            self.steps.append({
                "step": 5,
                "title": "Verificación π = πP",
                "description": "Verificamos que π = πP",
                "verification": verification.tolist(),
                "original": steady_state.tolist(),
                "error": float(error),
                "valid": bool(error < 1e-10)
            })
            
            return {
                "success": True,
                "steady_state": steady_state.tolist(),
                "steps": self.steps
            }
            
        except np.linalg.LinAlgError:
            return {"error": "No se pudo resolver el sistema (matriz singular)"}
    
    def calculate_n_step_probabilities(self, initial_state, n_steps):
        """Calcula probabilidades después de n pasos"""
        steps = []
        current_state = np.array(initial_state, dtype=float)
        
        steps.append({
            "step": 0,
            "state": current_state.tolist(),
            "description": "Estado inicial"
        })
        
        for i in range(1, n_steps + 1):
            current_state = np.dot(current_state, self.P)
            steps.append({
                "step": i,
                "state": current_state.tolist(),
                "description": f"Después de {i} paso{'s' if i > 1 else ''}"
            })
        
        return steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        matrix = data['matrix']
        
        mc = MarkovChain(matrix)
        result = mc.calculate_steady_state()
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/n_steps', methods=['POST'])
def n_steps():
    try:
        data = request.json
        matrix = data['matrix']
        initial_state = data['initial_state']
        n_steps = data['n_steps']
        
        mc = MarkovChain(matrix)
        steps = mc.calculate_n_step_probabilities(initial_state, n_steps)
        
        return jsonify({"success": True, "steps": steps})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)