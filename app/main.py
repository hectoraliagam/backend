from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.schemas import ContactForm
from app.models import Contact, Base
from app.database import engine, SessionLocal
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hectoraliagam.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MY_MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MY_MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MY_MAIL_FROM"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

@app.post("/contact")
async def send_contact(form: ContactForm, db: Session = Depends(get_db)):

    contact = Contact(name=form.name, email=form.email, message=form.message)
    db.add(contact)
    db.commit()
    db.refresh(contact)

    message = MessageSchema(
        subject="New message from my portfolio",
        recipients=[os.getenv("MAIL_RECEIVER")],
        body=f"Name: {form.name}\nEmail: {form.email}\nMessage:\n{form.message}",
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"message": "Thank you for contacting me, I will respond to you immediately."}
