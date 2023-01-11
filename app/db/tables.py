from sqlalchemy import Column, ForeignKey, Integer, String, PrimaryKeyConstraint

from app.db.conn import Base, conn


class Cars(Base):
    __tablename__ = 'cars'
    car_id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50))
    model = Column(String(50))


class Rate(Base):
    __tablename__ = 'rate'
    rate_id = Column(Integer, primary_key=True, index=True)
    rate_name = Column(String(40))


class Rates(Base):
    __tablename__ = 'rates'
    __table_args__ = (
        PrimaryKeyConstraint('rate_id', 'car_id'),
    )
    rate_id = Column(Integer, ForeignKey('rate.rate_id', ondelete='CASCADE'),
                     index=True)
    car_id = Column(Integer, ForeignKey('cars.car_id', ondelete='CASCADE'), index=True)
    price = Column(Integer)
