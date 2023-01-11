from urllib.error import HTTPError

from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request

from app.db.tables import Base, conn, Cars

app = FastAPI()


@app.on_event("startup")
async def startup():
    Base.metadata.create_all()


@app.on_event("shutdown")
async def shutdown():
    pass


@app.post("/car")
async def add_new_car(req: Request, session=conn):
    if req.headers.get("Content-Type") != "application/json":
        return Response("Incorrect content-type", status_code=403)

    try:
        data = await req.json()
    except Exception as e:
        return Response("Incorrect json", status_code=403)

    if not ('brand' in data and 'model' in data):
        return Response("Incorrect schema", status_code=403)

    new_car = Cars(
        brand=data['brand'],
        model=data['model']
    )

    session.add(new_car)
    session.commit()
    return Response(str(new_car.car_id))


@app.get("/")
async def read_root(connection=conn):
    return "connection acquired"
