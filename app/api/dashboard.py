from fastapi import APIRouter

from app.api.opportunities import OPPORTUNITIES
from app.api.projects import PROJECTS
from app.api.tasks import ITEMS

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def dashboard_summary():
    return {
        "project_count": len(PROJECTS),
        "opportunity_count": len(OPPORTUNITIES),
        "work_item_count": len(ITEMS),
        "model": "public reference",
        "protected_layer": "CGS Sentinel AI Engine is excluded from this repository.",
    }
