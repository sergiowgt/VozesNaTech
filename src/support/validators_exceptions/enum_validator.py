from . import DomainValidationError

class EnumValidator:
    @staticmethod
    def validate(value: int, field_name: str, enum_class: Any):
        DomainValidationError.when(value not in list(enum_class), f"{field_name} must be in {enum_class}. [value={value}]")