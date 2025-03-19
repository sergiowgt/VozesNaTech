from fastapi import APIRouter
from sqlalchemy import text
from src.infra.adapters.database.db_handler import DbHandler
from src.infra.adapters.db_config.db_config import DbConfig

async def check_database():
    db_config = DbConfig()
    db_handler = DbHandler(db_config)

    session = None
    try:
        db_handler.open()
        session = db_handler.get_session()
    except Exception as e:
        return {"database": "offline", "error": str(e)}
    finally:
        db_handler.close()

    try:
        session.execute(text("SELECT 1"))
        return {"database": "online"}
    except Exception as e:
        return {"database": "offline", "error": str(e)}


health_route = APIRouter()
@health_route.get("/")
async def health_check():
    return {"status": "OK", "message": "'Vozes na Tech' Application is running"}

@health_route.get("/db")
async def healthdb_check():
    
    db_status = await check_database()
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
