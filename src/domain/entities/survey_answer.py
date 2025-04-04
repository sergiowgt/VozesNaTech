from dataclasses import dataclass
from datetime import date
from src.support.entities.base_class import BaseClass
from src.support.validators_exceptions.domain_validator import DomainValidator
from src.domain.config.config_attributes import DESCRIPTION_FIELD

@dataclass
class SurveyAnswer(BaseClass):
    _class_name= 'Resposta'
    _gender_name= 'da'
    order: int  = 0
    description: str = ""

    def validate(self):
        super().validate()
        DomainValidator.string_required(self.description, f'Descrição {self._repr}',min_len=DESCRIPTION_FIELD.min, max_len=DESCRIPTION_FIELD.max)