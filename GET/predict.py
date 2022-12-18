from fastapi import APIRouter
from dependencies import Wine

router = APIRouter(
        prefix="/api/predict",
        responses={404: {"description": "Not found"}},
    )


@router.get("/")
async def give_grade():
    return { "Vin parfait": "Un vin" }