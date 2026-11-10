from datetime import datetime, timedelta, timezone
import os
import jwt
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "interviewiq-development-secret-change-before-production"
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token