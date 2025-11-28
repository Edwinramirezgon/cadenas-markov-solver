# Cadenas de Markov - Aplicativo Semi-automatizado

## Descripción del Proyecto

Este aplicativo web permite resolver problemas de **Cadenas de Markov** de manera semi-automatizada, mostrando paso a paso cada uno de los cálculos realizados. Está desarrollado en Python con Flask y optimizado para despliegue en Vercel.

## Funcionalidades

### 1. Cálculo de Estado Estacionario
- Ingreso de matriz de transición (2x2 hasta 5x5)
- Validación de matriz estocástica
- Resolución del sistema π = πP paso a paso
- Verificación de resultados
- Presentación en decimales y fracciones

### 2. Probabilidades n-pasos
- Cálculo de probabilidades después de n transiciones
- Estado inicial configurable
- Visualización de la evolución paso a paso

## Ejemplo de Aplicación: Modelo Meteorológico

El aplicativo incluye un ejemplo práctico de predicción del clima con 3 estados:
- **Estado 1**: Soleado
- **Estado 2**: Nublado  
- **Estado 3**: Lluvioso

### Matriz de Transición
```
P = [0.7  0.2  0.1]
    [0.3  0.4  0.3]
    [0.2  0.6  0.2]
```

### Interpretación
- Si hoy está soleado, hay 70% de probabilidad de que mañana esté soleado
- Si hoy está nublado, hay 40% de probabilidad de que mañana siga nublado
- Si hoy llueve, hay 60% de probabilidad de que mañana esté nublado

## Instalación Local

1. **Clonar o descargar los archivos**
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```
4. **Abrir en navegador:** http://localhost:5000

## Despliegue en Vercel

1. **Subir archivos a repositorio GitHub**
2. **Conectar repositorio con Vercel**
3. **Vercel detectará automáticamente la configuración**

## Estructura del Proyecto

```
├── app.py              # Aplicación Flask principal
├── templates/
│   └── index.html      # Interfaz web
├── requirements.txt    # Dependencias Python
├── vercel.json        # Configuración Vercel
└── README.md          # Documentación
```

## Metodología Matemática

### Estado Estacionario
1. **Verificación**: Comprobar que P es estocástica (filas suman 1)
2. **Sistema**: Resolver π = πP equivalente a (P^T - I)π = 0
3. **Normalización**: Aplicar condición Σπᵢ = 1
4. **Solución**: Resolver sistema de ecuaciones lineales
5. **Verificación**: Comprobar que π = πP

### Probabilidades n-pasos
- Multiplicación iterativa: π(n) = π(0) × P^n
- Mostrar evolución paso a paso hasta convergencia

## Análisis de Resultados

El aplicativo permite analizar:
- **Convergencia**: Velocidad hacia el estado estacionario
- **Estabilidad**: Comportamiento a largo plazo
- **Distribución límite**: Probabilidades finales independientes del estado inicial

## Tecnologías Utilizadas

- **Backend**: Python 3.x, Flask, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Despliegue**: Vercel
- **Matemáticas**: Álgebra lineal, sistemas de ecuaciones

## Autor

Desarrollado para el curso de Investigación de Operaciones como aplicativo semi-automatizado para resolver Cadenas de Markov con visualización paso a paso.