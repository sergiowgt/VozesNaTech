from dataclasses import dataclass
from fastapi import FastAPI
import uvicorn
#from src.infra.adapters.orm.orm_define import start_mappers
from src.webapp.controllers import teste_route, health_route

@dataclass
class WebApp:
    app: FastAPI

    @staticmethod
    def config_routes(app: FastAPI) -> None:
        app.include_router(health_route, prefix="/health", tags=["Health Check"]) 
        app.include_router(teste_route, prefix="/teste", tags=["Teste Types"])
        #app.include_router(level_type_route, prefix="/level_types", tags=["Level Types"])
        #app.include_router(student_route, prefix="/students", tags=["Students"])
        #app.include_router(colaborator_route, prefix="/colaborators", tags=["Colaborators"])
        #app.include_router(group_route, prefix="/groups", tags=["Groups"])
        #app.include_router(group_schedule_route, prefix="/group_schedules", tags=["Group Schedules"])
        #app.include_router(group_student_route, prefix="/group_students", tags=["Group Students"])
        #app.include_router(group_colaborator_route, prefix="/group_colaborators", tags=["Group Colaborators"])

    @staticmethod
    def execute() -> None:
        #start_mappers()
        #app = FastAPI(title=webapp_settings.title, version=webapp_settings.version, debug=webapp_settings.debug)
        app = FastAPI()
        WebApp.config_routes(app)
        uvicorn.run(app, host='127.0.0.1', port=5000)