from dataclasses import dataclass

@dataclass
class LoginModel:
    email: str = ''
    password: str = ''
