from jose import JWTError, jwt
from  datetime import datetime, timedelta
from . import schemas, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .database import get_db
from sqlalchemy.orm import Session
from .config import settings

oauth2_schme = OAuth2PasswordBearer(tokenUrl='login')

# three things are requried here,

# 1 Secrete Key

# 2 Algoritham

# 3 Expriation time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_acess_token(token: str, credential_exception):
    
    try:
        palyload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id : str = palyload.get("user_id")

        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_schme),db: Session = Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail=f"Could not validate credentials",
                                         headers={"www-Authenticate": "Bearer"})
    token = verify_acess_token(token=token,credential_exception=credential_exception)
    
    user = db.query(models.User).filter(models.User.id == token.id).first()


    return user