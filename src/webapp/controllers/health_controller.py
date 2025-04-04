from fastapi import APIRouter, Depends
from sqlalchemy import text
from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig

async def check_database(db_config: DbConfig):
    print(db_config.db_name)
    db_handler = DbHandler(db_config)

    try:
        db_handler.open()
        session = db_handler.get_session()
        session.execute(text("SELECT 1"))
        return {"database": "online"}
    except Exception as e:
        return {"database": "offline", "error": str(e)}
    finally:
        db_handler.close()

def create_health_router(db_config: DbConfig):
    health_route = APIRouter()

    async def health_check():
        return {"status": "OK", "message": "'Vozes na Tech' Application is running"}

    @health_route.get("/db")
    async def healthdb_check():
        db_status = await check_database(db_config)
        if db_status.get("database") == "online":
            return {
                "status": "OK",
                "message": "'Vozes na Tech' Application is running",
                "database": "connected"
            }
        else:
            return {
                "status": "Error",
                "message": "Database connection failed",
                "details": db_status
            }
    
    return health_route