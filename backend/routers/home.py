from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Home"])

templates = Jinja2Templates(directory="backend/templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )

    