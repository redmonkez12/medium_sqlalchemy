from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import dotenv_values

Base = declarative_base()


def db_connect():
    config = dotenv_values(".env")
    username = config.get("DB_USERNAME")
    password = config.get("DB_PASSWORD")
    dbname = config.get("DB_NAME")

    print(f"postgresql+psycopg://{username}:{password}@localhost:5432/{dbname}")

    engine = create_engine(f"postgresql+psycopg://{username}:{password}@localhost:5432/{dbname}", echo=True)
    connection = engine.connect()

    return engine, connection


def create_tables_orm(engine):
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine, checkfirst=True)


def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    return session
