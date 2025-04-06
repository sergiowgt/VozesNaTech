from dataclasses import dataclass
from src.support.entities.base_class import BaseClass

@dataclass
class UserSurveyAnswer(BaseClass):
    _class_name= 'Resposta do Usuário'
    _gender_name= 'da'
    user_id: int  = 0
    survey_id: int  = 0
    survey_question_id: int  = 0
    survey_answer_id:int  = 0

    def validate(self):
        super().validate()