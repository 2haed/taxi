from fastapi import FastAPI
from databases import Database
import sqlalchemy

from app.db.config import settings
from app.db.tables import Cars

app = FastAPI()
SQLALCHEMY_DATABASE_URL = (
    f"postgresql:psycopg2://{settings.database.user}:{settings.database.password}@{settings.database.host}:{settings.database.port}/{settings.database.database}"
)
database = Database(SQLALCHEMY_DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

