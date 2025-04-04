from dataclasses import dataclass
from typing import Any, List
from sqlalchemy.orm.session import Session
from src.infra.adapters.database.idb_handler import IDbHandler
from .ibase_repository import IBaseRepository
from ..entities.base_class import BaseClass
from ..enums.status_enum import StatusEnum

@dataclass
class BaseRepository (IBaseRepository):
    _session: Session = NotImplementedError
    _entity: BaseClass = NotImplementedError

    def __init__(self, db: IDbHandler, entity: BaseClass):
        self._session = db.get_session()
        self._entity = entity

    def _make_query(self, id: int, only_active: bool = False) -> Any:
        query = self._session.query(self._entity).filter_by(id = id)
        if (only_active):
            query = query.filter(self._entity.status == StatusEnum.ATIVO)
        else:
            query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query

    def exists(self, id: int, only_active: bool = False) -> bool:
        return any(self._make_query(id, only_active).all())

    def get(self, id: int, only_active: bool = False) -> BaseClass:
        return self._make_query(id, only_active).first()

    def get_all(self, only_active: bool = False) -> List[BaseClass]:
        query = self._session.query(self._entity)
        if (only_active):
            query = query.filter(self._entity.status == StatusEnum.ATIVO)
        else:
            query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.all()