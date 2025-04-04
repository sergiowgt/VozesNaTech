from dataclasses import dataclass
from datetime import date
from src.support.entities.named_base_class import NamedClassBase

@dataclass
class BusinessArea(NamedClassBase):
    _class_name= 'Area de Atuação'
    _gender_name= 'da'

    def validate(self):
        super().validate()
