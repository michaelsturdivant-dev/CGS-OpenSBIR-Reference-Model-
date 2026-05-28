from fastapi import APIRouter

from app.models import Task

router = APIRouter(prefix="/work-items", tags=["work-items"])

ITEMS: list[Task] = []


@router.get("")
def list_items():
    return ITEMS


@router.post("")
def create_item(item: Task):
    ITEMS.append(item)
    return {"item": item, "note": "Reference tracking only. Production storage should use a configured database."}
