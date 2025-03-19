python3 -m venv .venv 
source .venv/bin/activate
pip install --upgrade pip
pip install sqlalchemy fastapi  python-dotenv unicorv

INSTALAÇÃO UBUNTU 20.04.6
ssh root@vps57609.publiccloud.com.br
sudo apt update && sudo apt upgrade -y
sudo apt-get install python3.13
scp -r /Users/sergiosousa/work/python-vozes-na-tech root@vps57609.publiccloud.com.br:/opt/vozesNaTech/webapp
