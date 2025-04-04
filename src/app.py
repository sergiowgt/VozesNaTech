from dataclasses import dataclass
from fastapi import FastAPI
import uvicorn
from src.infra.adapters.orm.orm_define import start_mappers
from src.infra.adapters.db_config.db_config import DbConfig
from src.webapp.controllers import teste_route, create_health_router, business_area_router

@dataclass
class WebApp:
    app: FastAPI

    @staticmethod
    def config_routes(app: FastAPI, db_config: DbConfig) -> None:
        app.include_router(create_health_router(db_config), prefix="/health", tags=["Health Check"]) 
        app.include_router(business_area_router, prefix="/business_area", tags=["Business Area Types"])
        #app.include_router(level_type_route, prefix="/level_types", tags=["Level Types"])
        #app.include_router(student_route, prefix="/students", tags=["Students"])
        #app.include_router(colaborator_route, prefix="/colaborators", tags=["Colaborators"])
        #app.include_router(group_route, prefix="/groups", tags=["Groups"])
        #app.include_router(group_schedule_route, prefix="/group_schedules", tags=["Group Schedules"])
        #app.include_router(group_student_route, prefix="/group_students", tags=["Group Students"])
        #app.include_router(group_colaborator_route, prefix="/group_colaborators", tags=["Group Colaborators"])

    @staticmethod
    def execute(db_config: DbConfig) -> None:
        start_mappers()
        #app = FastAPI(title=webapp_settings.title, version=webapp_settings.version, debug=webapp_settings.debug)
        app = FastAPI()
        WebApp.config_routes(app, db_config)
        uvicorn.run(app, host='127.0.0.1', port=8000)