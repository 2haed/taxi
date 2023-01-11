from sqlalchemy.orm import Session

from . import classes, tables


def get_cars(db: Session):
    return db.query(tables.Cars).first()


def get_rates(db: Session):
    return db.query(tables.Rates).first()


def get_rate(db: Session):
    return db.query(tables.Rate).first()


def create_car(db: Session):
    # fake_hashed_password = user.password + "notreallyhashed"
    # db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    car_brand = 'test_brand'
    car_model = 'test_model'
    db.add(Cars)
    db.commit()
    db.refresh(db_user)
    return db_user
