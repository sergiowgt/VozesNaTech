from dataclasses import dataclass
from datetime import date
from .user_update_model import UserUpdateModel

@dataclass
class UserResponseModel (UserUpdateModel):
    id: int = 0
    email: str = ''
    cell_phone: str = ''
    ethnicity: str = ''
    birth_date: date = None
    female_gender: bool = True