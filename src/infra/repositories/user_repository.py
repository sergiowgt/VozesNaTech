from dataclasses import dataclass
from src.support.repositories import CRUDRepository, NamedRepository
from src.infra.adapters.database.idb_handler import IDbHandler
from src.domain.entities import User
from src.support.enums.status_enum import StatusEnum

@dataclass
class UserRepository (CRUDRepository, NamedRepository):
    def __init__(self, db: IDbHandler):
        super().__init__(db, User)

    def get_by_email(self, email: str) -> User:
        query = self._session.query(self._entity).filter_by(email = email)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()

    def get_by_cellphone(self, cell_phone: str) -> User:
        query = self._session.query(self._entity).filter_by(cell_phone = cell_phone)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()