from fastapi import APIRouter

router = APIRouter(
        prefix="/api/model",
        responses={404: {"description": "Not found"}},
    )


@router.get("/")
async def get_model():
    return { "Modele": "Le fichier modèle" }