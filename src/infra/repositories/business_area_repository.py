from dataclasses import dataclass
from src.support.repositories import CRUDRepository, NamedRepository
from src.infra.adapters.database.idb_handler import IDbHandler
from src.domain.entities import BusinessArea

@dataclass
class UserRepository (CRUDRepository, NamedRepository):
    def __init__(self, db: IDbHandler):
        super().__init__(db, BusinessArea)