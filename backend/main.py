from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.home import router as home_router
from routers.cadastro import router as cadastro_router
from routers.dashboard import router as dashboard_router
from routers.login import router as login_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home_router)
app.include_router(cadastro_router)
app.include_router(dashboard_router)
app.include_router(login_router)
