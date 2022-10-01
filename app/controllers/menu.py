from http.client import HTTPException
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

# Get Menu by id
@router.get("/{id}", response_description="Get a single menu", response_model=MenuModel)
async def show_menu(id: str):
    if (menu := await db["menus"].find_one({"_id": id})) is not None:
        return menu

    raise HTTPException(status_code=404, detail=f"Menu {id} not found")

@router.get(
    "/date/{date}", response_description="List of menus by date", response_model=List[MenuModel]
)
async def list_menu_by_date(date: str):
    menus = await db["menus"].find({"date": date}).to_list(1000)
    return menus

@router.post("/", response_description="Add new menu", response_model=MenuModel)
async def create_menu(menu: MenuModel):
    menu = dict(menu)
    new_menu = await db["menus"].insert_one(menu)
    created_menu = await db["menus"].find_one({"_id": new_menu.inserted_id})
    return created_menu

@router.delete("/{id}", response_description="Delete menu")
async def delete_menu(id: str):
    delete_result = await db["menus"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return {"message": "Menu deleted successfully!"}
    return {"message": "Menu not found"}