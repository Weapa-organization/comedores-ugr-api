from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class MenuModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    entrante: dict = Field(...)
    principal: dict = Field(...)
    acompaniamiento: dict = Field(...)
    postre: dict = Field(...)
    date: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "entrante": {
                    "name": "Macarrones",
                    "alergenos": [
                        "Gluten"
                    ]
                },
                "principal": {
                    "name": "Pollo",
                    "alergenos": [
                        "Lacteos"
                    ]
                },
                "postre": {
                    "name": "Tarta de queso",
                    "alergenos": [
                        "Gluten"
                    ]
                },
                "date": "2022-09-18"
            }
        }

class UpdateMenuModel(BaseModel):
    entrante: Optional[dict] = Field(...)
    principal: Optional[dict] = Field(...)
    acompaniamiento: Optional[dict] = Field(...)
    postre: Optional[dict] = Field(...)
    date: Optional[str] = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "entrante": {
                    "name": "Macarrones",
                    "alergenos": [
                        "Gluten"
                    ]
                },
                "principal": {
                    "name": "Pollo",
                    "alergenos": [
                        "Lacteos"
                    ]
                },
                "postre": {
                    "name": "Tarta de queso",
                    "alergenos": [
                        "Gluten"
                    ]
                },
                "date": "2022-09-18"
            }
        }