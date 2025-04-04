from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig

class BaseController:
    def __init__(self, db_config: DbConfig) -> None:
        self.db = DbHandler(db_config)
        self.db.open()

    def __del__(self):
        self.db.session.invalidate()