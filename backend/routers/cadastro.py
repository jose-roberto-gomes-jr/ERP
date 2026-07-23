from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from schemas.cadastro import CadastroCreate
from database import SessionLocal
from models.usuario import Usuario
from pwdlib import PasswordHash

router = APIRouter(prefix="/auth", tags=["Autenticação de cadastro"])

templates = Jinja2Templates(directory="templates")


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

@router.post("/cadastrar")
async def cadastrar(usuario: UsuarioCreate):

    password_hash = PasswordHash.recommended()
    senha_hash = password_hash.hash(usuario.senha)
    
    db = SessionLocal()

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha = senha_hash
     )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    db.close()

    return {"mensagem": "Usuario cadastrado",
             "id": novo_usuario.id}
