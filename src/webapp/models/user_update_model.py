from dataclasses import dataclass
from datetime import date
from.named_insert_update_model import NamedInsertUpdateModel

@dataclass
class UserUpdateModel (NamedInsertUpdateModel):
    name: str = ''
    email: str = ''
    cell_phone: str = ''
    ethnicity: str = ''
    birth_date: date = None
    female_gender: bool = True