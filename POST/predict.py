from fastapi import APIRouter
from dependencies import Wine


router = APIRouter(
        prefix="/api/predict",
        responses={404: {"description": "Not found"}},
    )


@router.post("/")
async def rate_wine(wine: Wine):
    return { "Prédiction": "Je prédit que l'API marche!" }
    