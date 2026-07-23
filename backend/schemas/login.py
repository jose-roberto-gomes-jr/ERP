from pydantic import BaseModel, EmailStr

class LoginCreate(BaseModel):
    email: EmailStr
    senha: str