from fastapi import APIRouter

router = APIRouter(
        prefix="/api/model/description",
        responses={404: {"description": "Not found"}},
    )


@router.get("/")
async def describe():
    return { "Description": "Un modèle qui prédit la qualité d'une bouteille de vin" }