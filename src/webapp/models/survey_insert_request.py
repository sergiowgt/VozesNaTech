from pydantic import BaseModel, Field
from typing import List

class SurveyBusinessAreaInsertRequest(BaseModel):
    name: str

class SurveyAnswerInsertRequest(BaseModel):
    description: str
    business_area: SurveyBusinessAreaInsertRequest

class SurveyQuestionInsertRequest(BaseModel):
    description: str
    answers: List[SurveyAnswerInsertRequest]
    number_of_answers: int = Field(..., ge=1)

    def __init__(self, **data):
        super().__init__(**data)
        self.number_of_answers = len(self.answers)

class SurveyInsertRequest(BaseModel):
    name: str
    questions: List[SurveyQuestionInsertRequest]
    number_of_questions: int = Field(..., ge=1)

    def __init__(self, **data):
        super().__init__(**data)
        self.number_of_questions = len(self.questions)