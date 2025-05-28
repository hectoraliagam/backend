from pydantic import BaseModel, EmailStr, Field

class ContactBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    message: str = Field(..., min_length=1)

class ContactForm(ContactBase):
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Juan Pancho",
                "email": "juanelpancho@example.com",
                "message": "Hi Hector, I liked your portfolio. Let's talk!"
            }
        }
