#!/bin/bash

SERVICE_NAME="vozesnatech.service"

# Parar o serviço
echo "Parando o serviço $SERVICE_NAME..."
sudo systemctl stop $SERVICE_NAME

# Atualizar os fontes
if [ -d "VozesNaTech" ]; then
    echo "Removendo diretório existente VozesNaTech..."
    rm -rf VozesNaTech
fi

echo "Clonando repositório..."
git clone https://github.com/sergiowgt/VozesNaTech.git

echo "Copiando arquivo .env..."
cp .env VozesNaTech/.env

echo "Instalando dependências Python..."
pip install -r VozesNaTech/requirements.txt

# Reiniciar o serviço
echo "Reiniciando o serviço $SERVICE_NAME..."
sudo systemctl start $SERVICE_NAME

# Verificar status do serviço
echo "Verificando status do serviço $SERVICE_NAME..."
sudo systemctl status $SERVICE_NAME
