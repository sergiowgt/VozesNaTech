from dataclasses import dataclass
from src.domain.validators.domain_validator import DomainValidator
from src.domain.exceptions.domain_validation_error import DomainValidationError
from src.domain.enums.status_enum import StatusEnum

@dataclass
class ClassBase:
    _class_name= 'Classe Base'
    _gender_name= 'da'
    id: int = 0
    status: StatusEnum = StatusEnum.ATIVO

    @property
    def _repr(self)->str:
        return f'{self._gender_name} {self._class_name}'

    def validate(self)->None:
        DomainValidator.validate_id(self.id, f'Id {self._repr}')
        DomainValidationError.when(self.status not in list(StatusEnum), f'Status {self._repr} inválido. [Status={self.status}]')