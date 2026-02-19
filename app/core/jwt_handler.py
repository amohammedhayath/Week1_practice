import os
import datetime
from datetime import timedelta
from dotenv import load_dotenv
from jose import jwt, JWTError

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DEFAULT_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data: dict, expires_minutes: int = DEFAULT_EXPIRE_MINUTES):
    if not SECRET_KEY:
        raise ValueError("Invalid secret key")
    temp_data = data.copy()
    curr_time = datetime.datetime.utcnow()
    exp_time = curr_time + timedelta(minutes=expires_minutes)
    temp_data["exp"] = exp_time
    token = jwt.encode(temp_data, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid token")