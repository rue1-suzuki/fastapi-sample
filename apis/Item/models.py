from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, Uuid
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Item(Base):
    __tablename__ = 'items'
    uuid = Column(
        type_=Uuid,
        default=uuid4,
        primary_key=True,
        index=True,
        unique=True,
    )
    created_at = Column(
        type_=DateTime,
        default=datetime.now,
    )
    updated_at = Column(
        type_=DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )
    #
    name = Column(type_=String)
    price = Column(type_=Integer)
