#!/bin/bash

# Parar instância anterior
pkill -f "python main.py"

# Atualizar código
git pull origin main

# Ativar ambiente
source venv/bin/activate

# Instalar novas dependências
pip install -r requirements.txt

# Iniciar o bot
nohup python main.py > bot.log 2>&1 &

echo "Bot atualizado e iniciado!"
