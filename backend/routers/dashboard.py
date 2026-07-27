from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from backend.auth import usuario_atual

router = APIRouter(tags=["dashboard"])

templates = Jinja2Templates(directory="backend/templates")

@router.get("/dashboard")
async def home(request: Request, usuario_id: int = Depends(usuario_atual)):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )
