#!/bin/bash
echo "Instalando Sentinel OG..."

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

echo "Instalación completada. Ejecuta 'python main.py' para iniciar Sentinel OG."