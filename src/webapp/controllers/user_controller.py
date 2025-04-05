from fastapi import APIRouter, status, Response, Depends
from src.support.JWT.JWT_handler import JWTHandler
from fastapi_utils.cbv import cbv
from src.domain.entities import User
from src.infra.adapters.db_config.db_config import DbConfig
from src.support.controllers.base_controller import BaseController
from src.infra.repositories import UserRepository
from src.webapp.models import UserInsertModel, UserUpdateModel, UserResponseModel

from src.support.enums.status_enum import StatusEnum
from src.support.validators_exceptions.domain_validation_error import DomainValidationError
from src.support.validators_exceptions.password_validation_error import PasswordValidationError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_route = APIRouter()
user_router = APIRouter()

@cbv(user_router)
class UserController(BaseController):
    user_id: str = Depends(JWTHandler.verify_token) 

    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = UserRepository(self.db)
        self.entity_name = 'User'

    @user_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @user_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result
    
    @user_router.post("/", status_code=status.HTTP_200_OK)
    async def add(self, data: UserInsertModel):
        
        entity = self.default_repo.get_by_email(data.email)
        if (entity):
                return Response(f'An {self.entity_name} with this email already exists.[name={data.email}]')
        
        entity = self.default_repo.get_by_name(data.name)
        if (entity):
                return Response(f'An {self.entity_name} with this name already exists.[name={data.name}]')
        
        entity = self.default_repo.get_by_cellphone(data.cell_phone)
        if (entity):
                return Response(f'An {self.entity_name} with this cellphone already exists.[name={data.cell_phone}]')


        new_obj = User(id=1, status=StatusEnum.ATIVO, name=data.name, email=data.email, cell_phone=data.cell_phone, ethnicity=data.ethnicity, birth_date=data.birth_date, female_gender=data.female_gender, password=data.password)
        try:
            new_obj.validate()
        except DomainValidationError as domain_error:
            return Response(f'{str(domain_error)}', status_code=status.HTTP_400_BAD_REQUEST)
        except PasswordValidationError as password_error:
            return Response(f'{str(password_error)}', status_code=status.HTTP_400_BAD_REQUEST)
        except:        
            return Response(f'unknown error', status_code=status.HTTP_400_BAD_REQUEST)

        try:
            new_obj.password = pwd_context.hash(data.password)
            self.default_repo.add(new_obj)
            self.db.commit() 
        except:        
            return Response(f'Unknown database error', status_code=status.HTTP_400_BAD_REQUEST)
        
        user_response_model = UserResponseModel(name=new_obj.name, email=new_obj.email, cell_phone=new_obj.cell_phone, ethnicity=new_obj.ethnicity, birth_date=new_obj.birth_date, female_gender=new_obj.female_gender, id=new_obj.id)
        return user_response_model
    

    @user_router.put("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def update(self, id: int, data: UserUpdateModel):
        entity = self.default_repo.get_by_name(data.name)
        if entity:
            if entity.id != id:
                return Response(f'An {self.entity_name} with this name already exists.[name={data.name}]')

        entity = self.default_repo.get_by_email(data.email)
        if entity:
            if entity.id != id:
                return Response(f'An {self.entity_name} with this email already exists.[name={data.email}]')
            
        entity = self.default_repo.get_by_cellphone(data.cell_phone)
        if entity:
            if entity.id != id:
                return Response(f'An {self.entity_name} with this cell_phone already exists.[name={data.cell_phone}]')
     
        entity_to_update = self.default_repo.get(id=id)
        if (entity_to_update is None):
            return Response(f'{self.entity_name} not found.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        entity_to_update.name = data.name
        entity_to_update.email=data.email
        entity_to_update.cell_phone=data.cell_phone
        entity_to_update.ethnicity=data.ethnicity
        entity_to_update.birth_date=data.birth_date
        entity_to_update.female_gender=data.female_gender

        try:
            entity_to_update.validate()
        except DomainValidationError as domain_error:
            return Response(f'{str(domain_error)}', status_code=status.HTTP_400_BAD_REQUEST)
        except:        
            return Response(f'unknown error', status_code=status.HTTP_400_BAD_REQUEST)

        try:
            self.db.commit()
        except:        
            return Response(f'Unknown database error', status_code=status.HTTP_400_BAD_REQUEST)
        
        return
    
    @user_router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        entity = self.default_repo.get(id=id)
        if (entity is None):
            return Response(f'{self.entity_name} not found.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        entity.status = StatusEnum.LOGICAMENTE_DELETADO
        self.db.commit()
        return
                

user_route.include_router(user_router)