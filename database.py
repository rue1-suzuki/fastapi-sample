from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./db.sqlite3'
engine = create_engine(DATABASE_URL)


def get_session():
    Session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    return Session()
