from dataclasses import dataclass
from datetime import date
from src.support.entities.named_base_class import NamedClassBase

@dataclass
class Survey(NamedClassBase):
    _class_name= 'Questionario'
    _gender_name= 'do'

    def validate(self):
        super().validate()
