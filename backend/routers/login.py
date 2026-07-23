from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from schemas.login import LoginCreate
from database import SessionLocal
from models.usuario import Usuario
from pwdlib import PasswordHash

router = APIRouter(prefix="/auth", tags=["Autenticação de login"])


@router.post("/login")
async def login(usuario: LoginCreate):

    password_hash = PasswordHash.recommended()

    db = SessionLocal()

    usuario_db = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    db.close()

    if usuario_db is None :
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    senha_valida = password_hash.verify(usuario.senha, usuario_db.senha)
    if not senha_valida:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
        
    
    