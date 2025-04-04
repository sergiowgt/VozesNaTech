
from src.infra.adapters.db_config.db_config import DbConfig
from src.app import WebApp

if __name__ == '__main__':
    WebApp.execute(DbConfig())