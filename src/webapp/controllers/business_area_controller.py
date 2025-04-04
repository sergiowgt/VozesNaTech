from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from src.domain.entities.business_area import BusinessArea
from src.infra.adapters.db_config.db_config import DbConfig
from src.support.controllers.base_controller import BaseController
from src.infra.repositories.business_area_repository import BusinessAreaRepository
from src.webapp.models import BusinessAreaInsertModel, BusinessAreaUpdateModel

from src.support.enums.status_enum import StatusEnum


business_area_route = APIRouter()
business_area_router = InferringRouter()

@cbv(business_area_router)
class BusinessController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = BusinessAreaRepository(self.db)
        self.entity_name = 'Business Area'

    @business_area_router.get("/{id}/", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        result = self.default_repo.get(id=id)
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result

    @business_area_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        result = self.default_repo.get_all()
        if (result is None):
            return Response("", status_code=status.HTTP_404_NOT_FOUND)

        return result
    
    
    @business_area_router.post("/", status_code=status.HTTP_200_OK)
    async def add(self, data: BusinessAreaInsertModel):
        entity = self.default_repo.get_by_name(data.name)
        if (entity):
                return Response(f'An {self.entity_name} with this name already exists.[name={data.name}]')

        new_obj = BusinessArea(id=1, status=StatusEnum.ATIVO, name=data.name)
        new_obj.validate()
        self.default_repo.add(new_obj)
        self.db.commit()
        return new_obj
    

    @business_area_router.put("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def update(self, id: int, data: BusinessAreaUpdateModel):
        entity = self.default_repo.get_by_name(data.name)
        if entity:
            if entity.id != id:
                return Response(f'An {self.entity_name} with this name already exists.[name={data.name}]')

            
        entity_to_update = self.default_repo.get(id=id)
        if (entity_to_update is None):
            return Response(f'{self.entity_name} not found.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        entity_to_update.name = data.name
        entity_to_update.validate()
        self.db.commit()
        return
    
    @business_area_router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        entity = self.default_repo.get(id=id)
        if (entity is None):
            return Response(f'{self.entity_name} not found.[id={id}]', status_code=status.HTTP_404_NOT_FOUND)
        
        entity.status = StatusEnum.LOGICAMENTE_DELETADO
        self.db.commit()
        return
                

business_area_route.include_router(business_area_router)