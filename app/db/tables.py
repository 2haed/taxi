import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.db.config import settings
import psycopg2


SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://%s:%s@%s:%s/%s?charset=utf8' % (settings.database.user, settings.database.password, settings.database.host, settings.database.port, settings.database.database)
Base = declarative_base(create_engine(SQLALCHEMY_DATABASE_URL))


class Cars(Base):
    __tablename__ = 'cars'
    car_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    brand = sqlalchemy.Column(sqlalchemy.String(50))
    model = sqlalchemy.Column(sqlalchemy.String(50))


class Rate(Base):
    __tablename__ = 'rate'
    rate_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    rate_name = sqlalchemy.Column(sqlalchemy.String(40))


class Rates(Base):
    __tablename__ = 'rates'
    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint('rate_id', 'car_id'),
    )
    rate_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('rate.rate_id', ondelete='CASCADE'),
                                index=True)
    car_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('cars.car_id', ondelete='CASCADE'), index=True)
    price = sqlalchemy.Column(sqlalchemy.Integer)
