from fastapi import APIRouter, status, HTTPException, Depends
from src.support.JWT.JWT_handler import JWTHandler
from fastapi_utils.cbv import cbv
from src.infra.adapters.db_config.db_config import DbConfig
from src.support.controllers.base_controller import BaseController
from src.infra.repositories.survey_repository import SurveyRepository

survey_router = APIRouter()

@cbv(survey_router)
class SurveyController(BaseController):
    user_id: str = Depends(JWTHandler.verify_token) 

    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = SurveyRepository(self.db)
        self.entity_name = 'Survey'

    @survey_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.entity_name} not found.[id={id}]"
            )
        return result

    @survey_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No {self.entity_name} found."
            )
        return result

    @survey_router.get("/{id}/questions/", status_code=status.HTTP_200_OK)
    async def list_question(self, id: int):
        result = self.default_repo.list_question(survey_id=id)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.entity_name} not found.[id={id}]"
            )
        
        survey, _ = result[0]
        questions = [
            {
                "order": question.order,
                "description": question.description,
                "id": question.id,
                "status": question.status,
            }
            for _, question in result
        ]

        return {
            "name": survey.name,
            "status": survey.status,
            "questions": questions
        }
    

    @survey_router.get("/{id}/questions/{order}/", status_code=status.HTTP_200_OK)
    async def get_question(self, id:int, order:int):
        result = self.default_repo.get_question(survey_id=id, order=order)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.entity_name} not found.[id={id}]"
            )

        return {
            "survey_name": result.Survey.name,
            "survey_status": result.Survey.status,
            "question_order": result.SurveyQuestion.order,
            "question_description": result.SurveyQuestion.description,
            "question_id": result.SurveyQuestion.id,
            "question_status": result.SurveyQuestion.status
        }
    
    @survey_router.get("/{id}/questions/{question_id}/answer", status_code=status.HTTP_200_OK)
    async def list_anwser(self, id: int, question_id: int):
        result = self.default_repo.list_answer(survey_id=id, survey_question_id=question_id)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.entity_name} not found.[id={id}]"
            )
        
        survey, survey_question, _, _ = result[0]
        answers = [
            {
                "order": reg.SurveyAnswer.order,
                "description": reg.SurveyAnswer.description,
                "id": reg.SurveyAnswer.id,
                "business_area_name": reg.BusinessArea.name
            }
            for reg in result
        ]

        return {
            "survey_name": survey.name,
            "survey_status": survey.status,
            "question_order": survey_question.order,
            "question_description": survey_question.description,
            "answers": answers
        }

    @survey_router.get("/{id}/questions/{question_id}/answer/{order}/", status_code=status.HTTP_200_OK)
    async def get_anwser(self, id: int, question_id: int, order: int):
        result = self.default_repo.get_answer(survey_id=id, survey_question_id=question_id,order=order)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{self.entity_name} not found.[id={id}]"
            )

        return {
            "survey_name": result.Survey.name,
            "survey_status": result.Survey.status,
            "question_order": result.SurveyQuestion.order,
            "question_description": result.SurveyQuestion.description,
            "answer_order": result.SurveyAnswer.order,
            "answer_description": result.SurveyAnswer.description,
            "answer_id": result.SurveyAnswer.id,
            "business_area_name": result.BusinessArea.name
        }
