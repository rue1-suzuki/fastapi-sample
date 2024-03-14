from fastapi import Body

from database import get_session

from ..models import Item


def create(name: str = Body(), price: int = Body(),):
    item = Item(
        name=name,
        price=price,
    )

    db = get_session()
    db.add(item)
    db.commit()
    db.refresh(item)

    return item
