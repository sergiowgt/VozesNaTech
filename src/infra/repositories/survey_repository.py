from dataclasses import dataclass
from src.support.repositories import NamedRepository
from src.infra.adapters.database.idb_handler import IDbHandler
from src.domain.entities import Survey, SurveyQuestion, SurveyAnswer, BusinessArea
from src.support.enums.status_enum import StatusEnum

@dataclass
class SurveyRepository (NamedRepository):
    def __init__(self, db: IDbHandler):
        super().__init__(db, Survey)

    def list_question(self, survey_id: int):
        query = (
            self._session.query(Survey, SurveyQuestion)
            .join(SurveyQuestion, Survey.id == SurveyQuestion.survey_id)
            .filter(Survey.id == survey_id)
            .filter(Survey.status !=  StatusEnum.LOGICAMENTE_DELETADO)
            .filter(SurveyQuestion.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
        )

        return query.all()
    
    def get_question(self, survey_id: int, order: int):
        query = (
            self._session.query(Survey, SurveyQuestion)
            .join(SurveyQuestion, Survey.id == SurveyQuestion.survey_id)
            .filter(Survey.id == survey_id)
            .filter(SurveyQuestion.order == order)
            .filter(Survey.status !=  StatusEnum.LOGICAMENTE_DELETADO)
            .filter(SurveyQuestion.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
        )        

        return query.first()
    

    def list_answer(self, survey_id: int, survey_question_id: int):
        query = (
            self._session.query(Survey, SurveyQuestion, SurveyAnswer, BusinessArea)
            .join(SurveyQuestion, Survey.id == SurveyQuestion.survey_id)
            .join(SurveyAnswer, SurveyQuestion.id == SurveyAnswer.survey_question_id)
            .join(BusinessArea, SurveyAnswer.business_area_id == BusinessArea.id)
            .filter(Survey.id == survey_id)
            .filter(SurveyQuestion.id == survey_question_id)
            .filter(Survey.status !=  StatusEnum.LOGICAMENTE_DELETADO)
            .filter(SurveyQuestion.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
            .filter(SurveyAnswer.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
        )

        return query.all()
    
    def get_answer(self, survey_id: int, survey_question_id: int, order: int):
        query = (
            self._session.query(Survey, SurveyQuestion, SurveyAnswer, BusinessArea)
            .join(SurveyQuestion, Survey.id == SurveyQuestion.survey_id)
            .join(SurveyAnswer, SurveyQuestion.id == SurveyAnswer.survey_question_id)
            .join(BusinessArea, SurveyAnswer.business_area_id == BusinessArea.id)
            .filter(Survey.id == survey_id)
            .filter(SurveyQuestion.id == survey_question_id)
            .filter(SurveyAnswer.order == order)
            .filter(Survey.status !=  StatusEnum.LOGICAMENTE_DELETADO)
            .filter(SurveyQuestion.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
            .filter(SurveyAnswer.status !=  StatusEnum.LOGICAMENTE_DELETADO) 
        )        

        return query.first()

