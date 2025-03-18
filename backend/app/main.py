import sys
import os
from datetime import timedelta

# Ensure the backend directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

# Import authentication functions
from app.auth.authentication import (
    create_access_token,
    get_current_user,
    oauth2_scheme,
    get_password_hash,
)

# Import API routers
from app.api.routes import router as main_router
from app.api.inventory_routes import router as inventory_router
from app.api.registration_routes import router as registration_router

# Import database setup
from app.database.connection import engine
from app.database.models import Base

# JWT token expiration configuration
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI app
app = FastAPI()

# Initialize the database (create tables if they don't exist)
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(main_router)
app.include_router(inventory_router)
app.include_router(registration_router)

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login endpoint to generate JWT token for valid users.
    """
    # Replace with actual user verification logic from the database
    if form_data.username != "user" or form_data.password != "password":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    """
    Example protected route that requires authentication.
    """
    return {"message": "You are accessing a protected route", "user": current_user}

@app.get("/")
def read_root():
    return {"message": "Welcome to BackTrackIt API"}
