from fastapi import APIRouter
from dependencies import Wine


router = APIRouter(
        prefix="/api/model/retrain",
        responses={404: {"description": "Not found"}},
    )


@router.post("/")
async def retrain():
    return {"resultat": "L'API à été ré-entrainée"}