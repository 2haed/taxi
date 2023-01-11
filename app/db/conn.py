import sqlalchemy.orm
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.db.config import settings

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
    settings.database.user, settings.database.password, settings.database.host, settings.database.port,
    settings.database.database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(bind=engine)


def get_conn() -> sqlalchemy.orm.Session:
    with SessionLocal() as session:
        yield session


conn = Depends(get_conn)
