from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from backend.schemas.login import LoginCreate
from backend.database import SessionLocal
from backend.models.usuario import Usuario
from pwdlib import PasswordHash
from backend.auth import criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação de login"])

templates = Jinja2Templates(directory="backend/templates")

password_hash = PasswordHash.recommended()



@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@router.post("/login")
async def login(usuario: LoginCreate, response: Response):


    db = SessionLocal()

    usuario_db = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    db.close()

    if usuario_db is None :
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    senha_valida = password_hash.verify(usuario.senha, usuario_db.senha)
    if not senha_valida:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    token = criar_token(usuario_db.id)

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age = 4  * 60 * 60,    
    )
    return {"mensagem": "login realizado com sucesso"}
    
    