from fastapi import APIRouter
from app.models import MenuModel
from typing import List
from app.database import db


router = APIRouter(
    prefix="/api/v1/menus"
)

@router.get(
    "/", response_description="List all students", response_model=List[MenuModel]
)
async def list_menu():
    students = await db["menus"].find().to_list(1000)
    return students