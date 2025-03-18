from dataclasses import dataclass
import os

@dataclass
class DbConfig:
    driver =  os.environ.get('DB_DRIVER', '')
    host =  os.environ.get('DB_HOST', '')
    db_name = os.environ.get('DB_NAME', '')
    user = os.environ.get('DB_USER', '')
    password = os.environ.get('DB_PASSWORD', '')
    echo = os.environ.get('DB_ECHO', '')
    timeout = os.environ.get('DB_TIMEOUT', 0)