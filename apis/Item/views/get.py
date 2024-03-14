from uuid import UUID

from fastapi import HTTPException, Path

from database import get_session

from ..models import Item


def get(item_id: UUID = Path()):
    db = get_session()

    item: Item | None = db.query(Item).get(item_id)
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    db.close()

    return item
