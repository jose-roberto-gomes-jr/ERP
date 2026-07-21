from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from schemas.usuario import UsuarioCreate

router = APIRouter(prefix="/auth", tags=["Autenticação"])

templates = Jinja2Templates(directory="templates")


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

@router.post("/cadastrar")
async def cadastrar(usuario: UsuarioCreate): 

    print(usuario)

    return {
        "Mensagem": "Dados recebidos"
    }