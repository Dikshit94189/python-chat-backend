from fastapi import FastAPI

from app.database.database import Base, engine

# Import models
from app.models.user import User

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Flutter Chat Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Backend Running 🚀"
    }