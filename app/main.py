from fastapi import FastAPI
from app.routers import recommend
from app.core.config import settings

app = FastAPI(title="Sistema de Recomendação Personalizado")

app.include_router(recommend.router)

@app.get("/")
def read_root():
    return {"message": "API de Recomendação Personalizada Online"}