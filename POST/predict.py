from fastapi import APIRouter
from dependencies import Wine


router = APIRouter(
        prefix="/api/predict",
        responses={404: {"description": "Not found"}},
    )


@router.post("/")
async def create_wine(wine: Wine):
    return wine