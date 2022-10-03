import motor.motor_asyncio
from app.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client.ComedoresUGR

def menu_helper(menu) -> dict:
    return {
        "id": str(menu["_id"]),
        "entrante": menu["entrante"],
        "principal": menu["principal"],
        "acompaniamiento": menu["acompaniamiento"],
        "postre": menu["postre"],
        "date": menu["date"],
    }