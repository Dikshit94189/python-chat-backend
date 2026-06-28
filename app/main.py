from fastapi import FastAPI

from app.database.database import Base, engine

# Import models
from app.models.user import User

# Import routes
from app.routes.user_routes import router as user_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Flutter Chat Backend",
    version="1.0.0"
)

# Register routes
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "Backend Running 🚀"
    }
