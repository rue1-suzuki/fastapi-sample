from fastapi import Query

from database import get_session

from ..models import Item


def list(name: str | None = Query(default=None), price: int | None = Query(default=None),):
    db = get_session()
    items = db.query(Item)
    db.close()

    if name is not None:
        items = items.filter(Item.name.contains(name))

    if price is not None:
        items = items.filter(Item.price == price)

    return items.order_by(Item.updated_at).all()
