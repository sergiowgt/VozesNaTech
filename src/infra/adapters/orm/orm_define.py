from src.domain.entities import User, BusinessArea, Survey, SurveyQuestion, SurveyAnswer
from .database_schema import mapper_registry, user_schema, business_area_schema, survey_schema, survey_question_schema, survey_answer_schema

def start_mappers():
    mapper_registry.map_imperatively(User, user_schema)
    mapper_registry.map_imperatively(BusinessArea, business_area_schema)
    mapper_registry.map_imperatively(Survey, survey_schema)
    mapper_registry.map_imperatively(SurveyQuestion, survey_question_schema)
    mapper_registry.map_imperatively(SurveyAnswer, survey_answer_schema)