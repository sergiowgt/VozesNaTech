python3 -m venv .venv 
source .venv/bin/activate
pip install --upgrade pip
pip install sqlalchemy fastapi  python-dotenv unicorv
brew install mysql pkg-config
export PATH="/usr/local/mysql/bin:$PATH"
source ~/.zshrc



INSTALAÇÃO UBUNTU 20.04.6
ssh root@vps57609.publiccloud.com.br
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3.13
python3.13 --version
sudo apt install mysql-client
mysql --version

alembic init alembic
alembic revision --autogenerate -m "descrição da migração"

pwd


rm -rf VozesNaTech

./atualizar_vozesnatech.sh



git clone https://github.com/sergiowgt/VozesNaTech.git



http://vps57609.publiccloud.com.br:8000/health/db

http://vps57609.publiccloud.com.br:8000/docs


