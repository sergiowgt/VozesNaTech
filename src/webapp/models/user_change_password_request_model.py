from dataclasses import dataclass

@dataclass
class UserChangePasswordRequestModel:
    old_password: str = ''
    new_password: str = ''