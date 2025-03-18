# authentication.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# JWT configuration
SECRET_KEY = "your_secret_key_here"  # Replace with a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme instance; tokenUrl should match your login endpoint (e.g., "/token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from auth.utils import (
    hashed_password, verify_password,create_access_token,verify_token
)
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            staus_code= status.HTTP_401_UNAUTHORIZED,)
            detail="Invalid token"
            headers={"WWW-Authenticate:","Beaer"}
        )
    return Payload
def Login_user(username:str,password:str,db_user)-> Optional[str]:
    if not db_user or not verify_password(password,db_user.hashed_password):
        return None
    access_token_expires=timedelta(minutes=30)
    token_data = {"sub":db_user.username}
    return create_access_token(
        data=token_data,
        expires_delta=access_token_expires
    )