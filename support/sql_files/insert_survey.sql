DELETE FROM Survey;
DELETE FROM SurveyAnswer;
DELETE FROM SurveyQuestion;

INSERT INTO Survey (id, status, name) VALUES
(1, 1, 'Vozes do Futuro');

INSERT INTO SurveyAnswer (
    id,
    status,
    description,
    order,
    survey_question_id,
    business_area_id
  )
VALUES (
    id:int,
    status:int,
    'description:varchar',
    order:int,
    survey_question_id:int,
    business_area_id:int
  );
  
  
  INSERT INTO SurveyQuestion (id, status, description, survey_id, order)
  VALUES (
      id:int,
      status:int,
      'description:varchar',
      survey_id:int,
      order:int
    );