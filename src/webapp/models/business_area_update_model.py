from dataclasses import dataclass
from.named_insert_update_model import NamedInsertUpdateModel

@dataclass
class BusinessAreaUpdateModel (NamedInsertUpdateModel):
    name: str = ''