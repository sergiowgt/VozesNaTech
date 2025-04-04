from dataclasses import dataclass
from datetime import date
from src.domain.config.config_attributes import EMAIL_FIELD, CELLPHONE_FIELD, BIRTH_DATE_FIELD
from src.support.validators_exceptions.domain_validator import DomainValidator
from src.support.entities.named_base_class import NamedClassBase
from src.support.validators_exceptions.domain_validation_error import DomainValidationError

@dataclass
class User(NamedClassBase):
    _class_name= 'Classe Base Pessoa'
    _gender_name= 'da'
    email: str = ''
    cell_phone: str = ''
    ethnicity: str = ''
    birth_date: date = None
    female_gender: bool = True

    def validate(self):
        super().validate() 
        DomainValidator.validate_email(self.email, f'email {self._repr}',min_len=EMAIL_FIELD.min, max_len=EMAIL_FIELD.max)
        DomainValidator.validate_cell_phone(self.cell_phone, f'Celular {self._repr}', CELLPHONE_FIELD.exact)
        DomainValidator.validate_birth_date(self.birth_date, f'Data Nascimento {self._repr}', BIRTH_DATE_FIELD.min, BIRTH_DATE_FIELD.max)
        DomainValidationError.when(not isinstance(self.female_gender, bool), "Identificação como gênero feminino não é válido")
        DomainValidationError.when(isinstance(self.ethnicity, str) is False, "Raça/Etnia não é uma string")
        DomainValidationError.when(self.ethnicity is None, 'Raça/Etnia está vazio')
 