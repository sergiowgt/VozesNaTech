from dataclasses import dataclass
from .base_class import BaseClass
from src.support.validators_exceptions.domain_validator import DomainValidator
from src.support.entities.base_config_atributtes import NAME_FIELD

@dataclass
class NamedClassBase(BaseClass):
    _class_name= 'NamedClassBase'
    _gender_name= 'do'
    name: str = ''

    def validate(self)->None:
        super().validate()
        DomainValidator.string_required(self.name, f'Nome {self._gender_name} {self._class_name}', exact_len=NAME_FIELD.exact, min_len=NAME_FIELD.min, max_len=NAME_FIELD.max)