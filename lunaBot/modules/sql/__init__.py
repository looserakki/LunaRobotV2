import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from lunaBot import DATABASE_URL, LOGGER


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL, client_encoding="utf8")
    LOGGER.info("PostgreSQL Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


