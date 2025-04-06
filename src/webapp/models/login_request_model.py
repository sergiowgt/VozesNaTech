from dataclasses import dataclass

@dataclass
class LoginRequestModel:
    email: str = ''
    password: str = ''
