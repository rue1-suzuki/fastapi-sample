from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, Uuid
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Item(Base):
    __tablename__ = 'items'
    uuid = Column(
        Uuid,
        primary_key=True,
        index=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    #
    name = Column(String, index=True)
    price = Column(Integer)
