from pydantic import BaseModel


class Cars(BaseModel):
    car_id: int
    brand: str
    model: str


class Rate(BaseModel):
    rate_id: int
    rate_name: str


class Rates(BaseModel):
    rate_id: int
    car_id: int
    price: int
