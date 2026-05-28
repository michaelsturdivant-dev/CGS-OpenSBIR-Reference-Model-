from fastapi import FastAPI

from app.api import artifacts, dashboard, opportunities, projects, tasks

app = FastAPI(
    title="CGS Sentinel OpenSBIR",
    description="Open-source reference model for SBIR, OTA, grant operations, compliance routing, and POAM tracking.",
    version="0.1.0",
)

app.include_router(projects.router)
app.include_router(opportunities.router)
app.include_router(tasks.router)
app.include_router(artifacts.router)
app.include_router(dashboard.router)


@app.get("/")
def root():
    return {
        "name": "CGS Sentinel OpenSBIR",
        "status": "reference-model",
        "docs": "/docs",
        "boundary": "Public reference model only; proprietary CGS Sentinel Engine logic is excluded.",
    }
