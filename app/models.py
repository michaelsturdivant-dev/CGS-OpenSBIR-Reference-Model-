from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str = Field(..., description="Project or initiative name")
    lane: str = Field(..., description="Public workflow lane such as SBIR, OTA, grant, EV, healthcare, workforce, or micro-community")
    description: str
    status: str = "intake"


class Opportunity(BaseModel):
    title: str
    sponsor: str
    pathway: str = Field(..., description="SBIR, STTR, OTA, grant, philanthropy, CDFI, or commercial")
    deadline: str | None = None
    notes: str | None = None


class Task(BaseModel):
    title: str
    owner: str | None = None
    priority: str = "medium"
    status: str = "open"
    evidence_required: str | None = None


class ArtifactRequest(BaseModel):
    artifact_type: str = Field(..., description="brief, charter, problem_statement, poam, email, or concept_note")
    source_summary: str
    lane: str | None = None
