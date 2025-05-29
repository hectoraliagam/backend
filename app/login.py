from fastapi import APIRouter, Form, HTTPException
from app.auth import create_access_token
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

USERNAME = os.getenv("ADMIN_USERNAME")
PASSWORD = os.getenv("ADMIN_PASSWORD")

@router.post("/login")
def login(username: str = Form(), password: str = Form()):
    if username == USERNAME and password == PASSWORD:
        token = create_access_token(data={"sub": username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
