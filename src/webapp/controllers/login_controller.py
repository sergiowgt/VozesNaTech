from fastapi import APIRouter, status, HTTPException
from fastapi_utils.cbv import cbv
from passlib.context import CryptContext
from src.infra.adapters.db_config.db_config import DbConfig
from src.support.controllers.base_controller import BaseController
from src.infra.repositories import UserRepository
from src.webapp.models import LoginRequestModel, LoginResponseModel
import jwt
from datetime import datetime, timedelta

from src.support.JWT.JWT_config import JWTConfig

# Configuração para hashing de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

login_route = APIRouter()
login_router = APIRouter()

def create_access_token(data: dict, secret_key, algorithm, expire_minutes):
    """Cria um token JWT"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

@cbv(login_router)
class LoginController(BaseController):
    def __init__(self):
        super().__init__(DbConfig())
        self.default_repo = UserRepository(self.db)
        self.entity_name = 'Login'
    
    @login_router.post("/", status_code=status.HTTP_200_OK, response_model=LoginResponseModel)
    async def validate(self, data: LoginRequestModel):
        # Busca o usuário pelo email
        entity = self.default_repo.get_by_email(data.email)
        
        if not entity:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )
        
        # Verifica se a senha está correta usando bcrypt
        if not pwd_context.verify(data.password, entity.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )
        
        # Gera o token JWT para o usuário autenticado
        jwt_config = JWTConfig()
        access_token = create_access_token(data={"sub": entity.email}, secret_key=jwt_config.SECRET_KEY, algorithm=jwt_config.ALGORITHM, expire_minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        return LoginResponseModel(access_token=access_token, token_type="bearer")
    
login_route.include_router(login_router)
