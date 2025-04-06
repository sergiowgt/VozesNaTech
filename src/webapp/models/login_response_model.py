from dataclasses import dataclass

@dataclass
class LoginResponseModel:
    access_token: str = ''
    token_type: str = ''