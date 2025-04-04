from dataclasses import dataclass
from typing import Any
from src.infra.adapters.database.idb_handler import IDbHandler
from .base_repository import BaseRepository
from ..entities.named_base_class import NamedClassBase
from ..enums.status_enum import StatusEnum

@dataclass
class NamedRepository (BaseRepository):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def get_by_name(self, name: str) -> NamedClassBase:
        query = self._session.query(self._entity).filter_by(name = name)
        query = query.filter(self._entity.status != StatusEnum.LOGICAMENTE_DELETADO)

        return query.first()