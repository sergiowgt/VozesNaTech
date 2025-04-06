from dataclasses import dataclass
from.named_insert_update_model import NamedInsertUpdateModel
from src.support.enums.status_enum import StatusEnum

@dataclass
class BusinessAreaResponseModel (NamedInsertUpdateModel):
    id: int = 0
    status: StatusEnum = StatusEnum.ATIVO
