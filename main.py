from dotenv import load_dotenv
from src.infra.adapters.db_config.db_config import DbConfig
from src.app import WebApp

if __name__ == '__main__':
    load_dotenv()
    db_config = DbConfig()
    WebApp.execute(db_config)