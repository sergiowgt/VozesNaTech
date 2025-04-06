from sqlalchemy import Index, MetaData, Column, ForeignKey, Integer, Table, BigInteger, VARCHAR, TypeDecorator, Date, Boolean
from sqlalchemy.orm import registry
from src.domain.config.config_attributes import DESCRIPTION_FIELD, EMAIL_FIELD, CELLPHONE_FIELD, CPF_FIELD
from src.support.entities.base_config_atributtes import NAME_FIELD

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

class StudentSituationType(TypeDecorator):
    impl = Integer

    def __init__(self, intflagtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._intflagtype = intflagtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._intflagtype(value)

class StatusType(TypeDecorator):
    impl = Integer
    cache_ok = True

    def __init__(self, intflagtype, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._intflagtype = intflagtype

    def process_bind_param(self, value, dialect):
        return value.value

    def process_result_value(self, value, dialect):
        return self._intflagtype(value)

class CpfType(TypeDecorator):
    impl = VARCHAR(CPF_FIELD.exact)

class CellPhoneType(TypeDecorator):
    impl = VARCHAR(CELLPHONE_FIELD.exact)

class DescriptionType(TypeDecorator):
    impl = VARCHAR(DESCRIPTION_FIELD.max)

class NameType(DescriptionType):
    impl = VARCHAR(NAME_FIELD.max)

class EmailType(TypeDecorator):
    impl = VARCHAR(EMAIL_FIELD.max)

class QuestionDescriptionType(TypeDecorator):
    impl = VARCHAR(8000)

list_base_schema = [
    Column('id', BigInteger, autoincrement=True, nullable = False, primary_key = True),
    Column('status', Integer, nullable = False)
]

list_description_type_schema = [x.copy() for x in list_base_schema] + [Column('description', DescriptionType, nullable = False)]
list_name_type_schema = [x.copy() for x in list_base_schema] + [Column('name', NameType, nullable = False)]
list_user_schema = ([x.copy() for x in list_name_type_schema] + 
    [      
        Column('email', EmailType, nullable = False), 
        Column('cell_phone', CellPhoneType, nullable = False), 
        Column('ethnicity', DescriptionType, nullable = False), 
        Column('birth_date', Date, nullable = False), 
        Column('female_gender', Boolean, nullable = False),
        Column('password', EmailType, nullable = False)
    ]
)

list_survey_schema = [x.copy() for x in list_name_type_schema] 
list_question_type_schema = [x.copy() for x in list_base_schema] + [Column('description', QuestionDescriptionType, nullable = False)]
list_survey_question_schema =  ([x.copy() for x in list_question_type_schema] + 
    [ 
        Column('survey_id', BigInteger, ForeignKey('Survey.id'),  nullable = False),
        Column('order', Integer, nullable = False)
    ])

list_survey_answer_schema =  ([x.copy() for x in list_question_type_schema] +
    [ 
        Column('order', Integer, nullable = False),
        Column('survey_question_id', BigInteger, ForeignKey('SurveyQuestion.id'), nullable = False), 
        Column('business_area_id', BigInteger, ForeignKey('BusinessArea.id'), nullable = False), 
    ])
list_business_area_schema = [x.copy() for x in list_name_type_schema] 


user_schema = Table(
    'User', 
    mapper_registry.metadata,
    *list_user_schema
)

survey_schema = Table(
    'Survey', 
    mapper_registry.metadata,
    *list_survey_schema
)

survey_question_schema = Table(
    'SurveyQuestion', 
    mapper_registry.metadata,
    *list_survey_question_schema,
    Index('ix_survey_question_survey_id', 'survey_id')
)

survey_answer_schema = Table(
    'SurveyAnswer', 
    mapper_registry.metadata,
    *list_survey_answer_schema,
    Index('ix_survey_answer_question_id', 'survey_question_id'),
    Index('ix_survey_answer_business_area_id', 'business_area_id')
)

business_area_schema = Table(
    'BusinessArea', 
    mapper_registry.metadata,
    *list_business_area_schema
)

list_user_survey_answer_schema =  ([x.copy() for x in list_base_schema] +
    [ 
        Column('user_id', BigInteger, ForeignKey('User.id'), nullable = False), 
        Column('survey_id', BigInteger, ForeignKey('Survey.id'), nullable = False), 
        Column('survey_question_id', BigInteger, ForeignKey('SurveyQuestion.id'), nullable = False), 
        Column('survey_answer_id', BigInteger, ForeignKey('SurveyAnswer.id'), nullable = False), 
    ])

user_survey_answer_schema = Table(
    'UserSurveyAnswer', 
    mapper_registry.metadata,
    *list_user_survey_answer_schema,
    Index('ix_user_survey_answer_user_id', 'user_id'),
    Index('ix_user_survey_answer_survey_id', 'survey_id'),
    Index('ix_user_survey_answer_question_id', 'survey_question_id'),
    Index('ix_user_survey_answer_id', 'survey_answer_id')
)