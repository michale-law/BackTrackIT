import sys
import os

# Ensure the "backend" directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from app.api.routes import router  # Ensure routes.py exists and is correct
from app.database.connection import engine
from app.database.models import Base  # Ensure models.py exists and defines Base

app = FastAPI()

# Initialize database
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to BackTrackIt API"}
