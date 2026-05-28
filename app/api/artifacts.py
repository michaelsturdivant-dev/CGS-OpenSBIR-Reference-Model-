from fastapi import APIRouter

from app.models import ArtifactRequest

router = APIRouter(prefix="/artifacts", tags=["artifacts"])


@router.post("/draft")
def draft_artifact(request: ArtifactRequest):
    return {
        "artifact_type": request.artifact_type,
        "lane": request.lane,
        "draft": f"Reference placeholder for {request.artifact_type}: {request.source_summary}",
        "boundary": "This endpoint is a public placeholder and does not include proprietary artifact generation logic.",
    }
