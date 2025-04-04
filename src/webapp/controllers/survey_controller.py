from fastapi import APIRouter, Depends, HTTPException
from typing import List
from src.models import SurveyInsertRequest
from .survey_service import SurveyService
from .dependencies import get_survey_service

router = APIRouter()

class SurveyController:
    @router.post("/surveys", response_model=SurveyInsertRequest)
    async def insert(survey: SurveyInsertRequest, service: SurveyService = Depends(get_survey_service)):
        try:
            return await service.insert(survey)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    """ @router.put("/surveys/{survey_id}", response_model=Survey)
    async def update(survey_id: int, survey_update: SurveyUpdate, service: SurveyService = Depends(get_survey_service)):
        try:
            return await service.update(survey_id, survey_update)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/surveys/{survey_id}", response_model=Survey)
    async def list(survey_id: int, service: SurveyService = Depends(get_survey_service)):
        try:
            survey = await service.get(survey_id)
            if survey is None:
                raise HTTPException(status_code=404, detail="Survey not found")
            return survey
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/surveys", response_model=List[Survey])
    async def list_all(service: SurveyService = Depends(get_survey_service)):
        try:
            return await service.get_all()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) """

# Adicione esta linha no final do arquivo para incluir as rotas
survey_controller = SurveyController()
