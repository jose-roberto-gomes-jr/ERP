from pydantic import BaseModel, EmailStr

class CadastroCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str