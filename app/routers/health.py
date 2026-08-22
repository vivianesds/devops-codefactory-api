from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Verificação de Saúde"])

@router.get("")
def health_check():
    return {"status": "saudavel", "banco_de_dados": "conectado"}