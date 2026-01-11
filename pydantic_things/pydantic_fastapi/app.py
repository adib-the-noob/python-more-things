# Fastapi with Dependency Injection and Pydantic Models

from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "My FastAPI App"
    admin_email: EmailStr = "admin@fastapi.com"


def get_settings_dependency() -> Settings:
    return Settings()

@app.post("/signup")
async def signup(user: UserSignup):
    return {
        "message": "User signed up successfully",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }

@app.get("/info")
async def get_settings(settings: Settings = Depends(get_settings_dependency)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email
    }
