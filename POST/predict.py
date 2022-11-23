from fastapi import APIRouter
from pydantic import BaseModel, Field

class Wine(BaseModel):
    fixed_acidity : float= Field(
        default=None, title="Acidité fixe : il s'agit de l'acidité naturelle du raisin comme l'acide malique ou l'acide tartrique.", gte=0
    )
    volatile_acidity: float= Field(
        default=None, title="Acidité volatile : l'acidité volatile d'un vin est constituée par la partie des acides gras comme l'acide acétique appartenant à la série des acides qui se trouvent dans le vin soit à l'état libre, soit à l'état salifié. L'acidité volatile donne au vin du bouquet.", gte=0
    )
    citric_acid: float= Field(
        default=None, title="Acide citrique : utilisé pour la prévention de la casse ferrique et participe au rééquilibrage de l'acidité des vins.", gte=0
    )
    residual_sugar: float = Field(
        default=None, title="Sucre résiduel : sucres (glucose + fructose) encore présents dans le vin après fermentation.", gte=0
    )
    chlorides: float = Field(
        default=None, title="Chlorures : matière minérale contenue naturellement dans le vin (sel, magnésium...)", gte=0
    )
    free_sulfur_dioxide: int = Field(
        default=None, title="Sulfites libres : exhacerbent les propriétés antioxydantes du vin", gte=0
    )
    total_sulfur_dioxide: int = Field(
        default=None, title="Sulfites libres + Sulfites liées à la réaction avec d'autres molécules du vin", gte=0
    )
    density: float= Field(
        default=None, title="Densité du vin (g/l)", gte=0
    )
    pH: float= Field(
        default=None, title="Le pH du vin", gte=0, lte=14
    )
    sulphates: float = Field(
        default=None, title="Sulfates : sels composés d'anions SO4(2-) != sulfites", gte=0
    )
    alcohol: float = Field(
        default=None, title="degré d'alcool", gte=0
    )
    quality: int = Field(
        default=None, title="Qualité générale : note comprise en 0 et 10", gte=0, lte = 10
    )
    id: int


router = APIRouter(
        prefix="/api/predict",
        responses={404: {"description": "Not found"}},
    )


@router.post("/")
async def create_wine(wine: Wine):
    return wine