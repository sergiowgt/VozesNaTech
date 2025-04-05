from src.support.entities.base_config_atributtes import FieldLen

DESCRIPTION_FIELD = FieldLen(5, 100, 0)
EMAIL_FIELD = FieldLen(0, 100, 0)
CELLPHONE_FIELD = FieldLen(0, 0, 11)
CPF_FIELD = FieldLen(0, 0, 11)
BIRTH_DATE_FIELD = FieldLen(16, 80, 0)
PASSWORD_FIELD = FieldLen(6, 12, 0)