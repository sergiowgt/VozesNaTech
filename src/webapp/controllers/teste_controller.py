from fastapi import APIRouter, status, Response
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

teste_route = APIRouter()
teste_router = InferringRouter()

@cbv(teste_router)
class TesteController():
    def __init__(self):
        ...
        #super().__init__(DbConfig())
       #self.default_repo = LevelTypeRepository(self.db)

    @teste_router.get("/{id}", status_code=status.HTTP_200_OK)
    async def get(self, id: int):
        return Response("", status_code=status.HTTP_204_NO_CONTENT)

        
    @teste_router.get("/", status_code=status.HTTP_200_OK)
    async def list(self):
        return Response("", status_code=status.HTTP_401_UNAUTHORIZED)

teste_route.include_router(teste_router)