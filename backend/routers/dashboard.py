from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["dashboard"])

templates = Jinja2Templates(directory="templates")

@router.get("/dashboard")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )