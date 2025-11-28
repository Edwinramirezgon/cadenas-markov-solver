#!/usr/bin/env python3
"""
Script para ejecutar la aplicación localmente
Instala dependencias automáticamente si no están disponibles
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala las dependencias necesarias"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
    except subprocess.CalledProcessError:
        print("❌ Error instalando dependencias")
        return False
    return True

def run_app():
    """Ejecuta la aplicación Flask"""
    try:
        from app import app
        print("🚀 Iniciando aplicación en http://localhost:6001")
        print("📊 Aplicativo de Cadenas de Markov listo")
        print("🔗 Presiona Ctrl+C para detener")
        app.run(debug=True, host='0.0.0.0', port=6001)
    except ImportError:
        print("❌ Error importando Flask. Instalando dependencias...")
        if install_requirements():
            from app import app
            app.run(debug=True, host='0.0.0.0', port=6001)
        else:
            print("❌ No se pudo instalar Flask")

if __name__ == "__main__":
    print("🔗 Cadenas de Markov - Aplicativo Semi-automatizado")
    print("=" * 50)
    
    # Verificar archivos
    required_files = ['app.py', 'templates/index.html', 'requirements.txt']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Archivos faltantes: {missing_files}")
        sys.exit(1)
    
    print("📁 Todos los archivos presentes")
    run_app()