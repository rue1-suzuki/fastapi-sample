from uuid import UUID

from fastapi import Body, HTTPException, Path

from database import get_session

from ..models import Item


def update(item_id: UUID = Path(), name: str | None = Body(default=None), price: int | None = Body(default=None),):
    db = get_session()

    item: Item | None = db.query(Item).get(item_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    if not name is None:
        item.name = name

    if not price is None:
        item.price = price

    db.commit()
    db.refresh(item)

    return item
