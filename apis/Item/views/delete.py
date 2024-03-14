from uuid import UUID

from fastapi import HTTPException, Path

from database import get_session

from ..models import Item


def delete(item_id: UUID = Path()):
    db = get_session()

    item: Item | None = db.query(Item).get(item_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    db.delete(item)
    db.commit()

    return item
