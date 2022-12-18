from fastapi import APIRouter

router = APIRouter(
        prefix="/api/predict",
        responses={404: {"description": "Not found"}},
    )


@router.get("/")
async def root():
    return { "Prédiction": "Je prédit que l'API marche!" }