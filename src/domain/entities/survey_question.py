from dataclasses import dataclass
from src.domain.config.config_attributes import DESCRIPTION_FIELD
from src.support.validators_exceptions.domain_validator import DomainValidator
from src.support.entities.base_class import BaseClass

@dataclass
class SurveyQuestion(BaseClass):
    _class_name= 'Pergunta'
    _gender_name= 'da'
    order: int = 9
    description: str = ""

    def validate(self):
        super().validate()
        DomainValidator.string_required(self.description, f'Descrição {self._repr}',min_len=DESCRIPTION_FIELD.min, max_len=DESCRIPTION_FIELD.max)