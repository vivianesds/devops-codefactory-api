from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="CodeFactory Solutions API",
    description="API REST para padronização de processos DevOps.",
    version="1.0.0"
)

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"mensagem": "API da CodeFactory executando com sucesso!"}