#!/bin/bash

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y python3-pip python3-venv git ffmpeg

# Configurar ambiente Python
python3 -m venv venv
source venv/bin/activate

# Instalar dependências Python
pip install -r requirements.txt

# Configurar permissões
chmod +x main.py

echo "Instalação concluída! Configure as credenciais antes de executar."
