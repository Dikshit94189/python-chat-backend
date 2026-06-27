from fastapi import FastAPI

from app.config.settings import DATABASE_URL

app = FastAPI()

@app.get("/")
def home():
    return {
        "database": DATABASE_URL
        # "message": "Welcome to Flutter Chat Backend 🚀"
    }