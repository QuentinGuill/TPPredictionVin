from fastapi import APIRouter
from dependencies import Wine


router = APIRouter(
        prefix="/api/model",
        responses={404: {"description": "Not found"}},
    )


@router.put("/")
async def add_wine(wine: Wine):
    return {"Resultat": "Le vin a bien été ajouté"}