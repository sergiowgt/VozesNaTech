from dataclasses import dataclass
from typing import Any
from src.infra.adapters.database.idb_handler import IDbHandler
from .base_repository import BaseRepository
from ..entities.base_class import BaseClass
from ..enums.status_enum import StatusEnum

@dataclass
class CRUDRepository (BaseRepository):
    def __init__(self, db: IDbHandler, entity: Any):
        super().__init__(db, entity)

    def add(self, obj: BaseClass) -> None:
        obj.id = None
        obj.status = StatusEnum.ATIVO
        self._session.add(obj)
        self._session.flush()

    def delete(self, obj: BaseClass) -> None:
        obj.status = StatusEnum.LOGICAMENTE_DELETADO