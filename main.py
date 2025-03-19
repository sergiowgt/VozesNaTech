from dotenv import load_dotenv
from sqlalchemy import text
from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig
from src.app import WebApp

if __name__ == '__main__':
    load_dotenv()
    WebApp.execute()