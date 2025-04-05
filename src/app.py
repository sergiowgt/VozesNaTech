from dataclasses import dataclass
from fastapi import FastAPI
import uvicorn
from fastapi.openapi.utils import get_openapi
from src.infra.adapters.orm.orm_define import start_mappers
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers import create_health_router, business_area_router, user_router, login_router, survey_router


@dataclass
class WebApp:
    app: FastAPI

    @staticmethod
    def config_routes(app: FastAPI, db_config: DbConfig) -> None:
        app.include_router(create_health_router(db_config), prefix="/health", tags=["Health Check"])
        app.include_router(login_router, prefix="/login", tags=["Login"])
        app.include_router(business_area_router, prefix="/business_areas", tags=["Business Areas"])
        app.include_router(user_router, prefix="/users", tags=["Users"])
        app.include_router(survey_router, prefix="/surveys", tags=["Surveys"])

    @staticmethod
    def execute(db_config: DbConfig) -> None:
        # Inicializa os mapeadores do ORM e cria a aplicação FastAPI
        start_mappers()
        
        # Instância do FastAPI
        app = FastAPI()

        def custom_openapi(app):
            if app.openapi_schema:
                return app.openapi_schema
            
            openapi_schema = get_openapi(
                title="Minha API",
                version="1.0.0",
                description="Documentação da API com JWT Auth",
                routes=app.routes,
            )
            openapi_schema["components"]["securitySchemes"] = {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
            for path in openapi_schema["paths"].values():
                for operation in path.values():
                    operation["security"] = [{"BearerAuth": []}]
            app.openapi_schema = openapi_schema
            return app.openapi_schema

        app.openapi = lambda: custom_openapi(app)

        # Configura as rotas da aplicação
        WebApp.config_routes(app, db_config)

        # Executa o servidor Uvicorn na porta 8000
        uvicorn.run(app, host='127.0.0.1', port=8000)
