from dotenv import load_dotenv
import os
from src.infra.adapters.db_config.db_config import DbConfig
from src.app import WebApp

if __name__ == '__main__':
    load_dotenv()
    WebApp.execute(DbConfig(), host=os.environ.get('APP_HOST', ''), port=os.environ.get('APP_PORT', 8000))
