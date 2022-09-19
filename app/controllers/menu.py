from fastapi import APIRouter
from app.models import MenuModel
from typing import List
from app.database import db


router = APIRouter(
    prefix="/api/v1/menus"
)

@router.get(
    "/", response_description="List all menus", response_model=List[MenuModel]
)
async def list_menu():
    menus = await db["menus"].find().to_list(1000)
    return menus

# get menu by date
@router.get(
    "/{date}", response_description="List of menus by date", response_model=List[MenuModel]
)
async def list_menu_by_date(date: str):
    menus = await db["menus"].find({"date": date}).to_list(1000)
    return menus
