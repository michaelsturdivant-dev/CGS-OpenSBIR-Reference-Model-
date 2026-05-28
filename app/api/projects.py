from fastapi import APIRouter

from app.models import Project
from app.services.routing import classify_lane

router = APIRouter(prefix="/projects", tags=["projects"])

PROJECTS: list[Project] = []


@router.get("")
def list_projects():
    return PROJECTS


@router.post("")
def create_project(project: Project):
    routed_lane = classify_lane(project.description, default=project.lane)
    stored = project.model_copy(update={"lane": routed_lane})
    PROJECTS.append(stored)
    return {"project": stored, "routing_note": "Public reference routing only; proprietary Sentinel logic is excluded."}
