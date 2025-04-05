from datetime import date
import re
from .domain_validation_error import DomainValidationError
from .password_validation_error import PasswordValidationError
from dateutil.relativedelta import relativedelta

class DomainValidator:
    @staticmethod
    def string_required(value: str, field_name: str, exact_len: int = 0, min_len: int = 0, max_len: int = 0) -> None:
        DomainValidationError.when(isinstance(value, str) is False, f"{field_name} não é uma string")
        DomainValidationError.when(value is None, f'{field_name} está vazio')

        value = value.strip()

        DomainValidationError.when(len(value) == 0, f'{field_name} não pode ser vazio')
        if (exact_len > 0):
            DomainValidationError.when(len(value) != exact_len, f'{field_name} deve ter tamanho de {exact_len}')
        else:
            DomainValidationError.when(min_len > 0 and len(value) < min_len, f'{field_name} deve ter tamanho minimo de {min_len}')
            DomainValidationError.when(max_len > 0 and len(value) > max_len, f'{field_name} deve ter tamanho máximo de {max_len}')

    @classmethod
    def validate_email(cls, value: str, field_name: str, min_len: int = 0, max_len: int = 0) -> None:
        cls.string_required(value, field_name, 0, min_len, max_len)
        value = value.strip()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        DomainValidationError.when(re.fullmatch(regex, value) is None, f'{field_name} não é um email valido')

    @classmethod
    def validate_cell_phone(cls, value: str, field_name: str, exact_len: int = 0) -> None:
        cls.string_required(value, field_name, exact_len, 0, 0)
        value = value.strip()

        regex = re.compile(r'([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})')
        DomainValidationError.when(re.fullmatch(regex, value) is False, f'{field_name} não é um telefone celular')

    @staticmethod
    def validate_id(value: int, field_name: str) -> None:
        DomainValidationError.when(isinstance(value, int) is False, f"{field_name} não é um inteiro")
        DomainValidationError.when(value <= 0, f'{field_name} deve ser um inteiro positivo. [Id={value}]')

    @staticmethod
    def validate_birth_date(birth_date: date, field_name: str, min_age: int=0, max_age: int=0) -> None:
        DomainValidationError.when(not isinstance(birth_date, date), f"{field_name} não é uma data válida")
        
        today = date.today()
        age = relativedelta(today, birth_date).years
        
        if min_age:
            DomainValidationError.when(age < min_age, f"{field_name} indica que a pessoa tem menos de {min_age} anos. [Idade={age}]")

        if max_age:
            DomainValidationError.when(age > max_age, f"{field_name} indica que a pessoa tem mais de {max_age} anos. [Idade={age}]")
    
        DomainValidationError.when(birth_date > today, f"{field_name} não pode ser uma data futura")

    @classmethod
    def validate_password(cls, value: str, field_name: str, min_len: int = 8, max_len: int = 20) -> None:
        value = value.strip()

        # Verifica o tamanho da senha
        PasswordValidationError.when(
            len(value) < min_len,
            f"{field_name} deve ter pelo menos {min_len} caracteres."
        )
        
        PasswordValidationError.when(
            len(value) > max_len,
            f"{field_name} não pode ter mais de {max_len} caracteres."
        )

        # Verifica se há pelo menos um caractere numérico
        has_numeric = any(char.isdigit() for char in value)
        
        # Verifica se há pelo menos um caractere alfabético
        has_alpha = any(char.isalpha() for char in value)
        
        # Verifica se há pelo menos um caractere maiúsculo
        has_uppercase = any(char.isupper() for char in value)
        
        # Verifica se há pelo menos um caractere especial
        has_special = any(not char.isalnum() for char in value)

        # Levanta exceção personalizada se algum critério não for atendido
        PasswordValidationError.when(
            not has_numeric,
            f"{field_name} deve conter pelo menos um número."
        )
        
        PasswordValidationError.when(
            not has_alpha,
            f"{field_name} deve conter pelo menos uma letra."
        )
        
        PasswordValidationError.when(
            not has_uppercase,
            f"{field_name} deve conter pelo menos uma letra maiúscula."
        )
        
        PasswordValidationError.when(
            not has_special,
            f"{field_name} deve conter pelo menos um caractere especial."
        )