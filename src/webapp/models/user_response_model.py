from dataclasses import dataclass

from src.support.enums.status_enum import StatusEnum
from .user_update_model import UserUpdateModel

@dataclass
class UserResponseModel (UserUpdateModel):
    id: int = 0
    status: StatusEnum = StatusEnum.ATIVO