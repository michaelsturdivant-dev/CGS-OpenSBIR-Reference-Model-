# CGS Sentinel OpenSBIR™

CGS Sentinel OpenSBIR™ is an open-source reference model for AI-assisted SBIR, OTA, grant operations, project intake, compliance routing, POAM tracking, artifact generation, and operational execution.

This repository is designed to help small businesses, nonprofits, universities, government-adjacent teams, and community infrastructure partners organize complex opportunities into clear execution workflows.

## Purpose

The purpose of this project is to provide a public reference model that demonstrates how AI-assisted operations can support:

- SBIR/STTR project development
- OTA concept packaging
- Grant opportunity tracking
- Project intake and classification
- Compliance routing
- Task and POAM management
- Artifact generation
- Community infrastructure planning
- Open-source collaboration

## What This Repository Includes

This public reference model may include:

- FastAPI backend structure
- SQLite MVP database pattern
- Project intake endpoints
- Opportunity intake endpoints
- Task and POAM tracking patterns
- Artifact placeholder workflows
- Sentinel-style routing logic
- Dashboard summary endpoints
- Example SBIR, grant, healthcare, EV, workforce, and micro-community use cases

## What This Repository Does Not Include

This repository does **not** include the full proprietary CGS Sentinel AI Engine™.

Excluded materials include:

- Proprietary CGS logic
- Private prompts
- Protected SBIR/STTR technical data
- Customer data
- Private partner information
- Commercial deployment playbooks
- Advanced orchestration logic
- API keys or secrets
- Internal strategy documents

## Open-Core Model

CGS Sentinel OpenSBIR™ is the public reference layer.

The protected commercial layer is the CGS Sentinel AI Engine™, which may include advanced agents, kernels, assistants, dashboards, integrations, compliance workflows, and managed deployment services.

## Intended Use Cases

This model can support:

- SBIR proposal preparation
- OTA readiness planning
- Federal grant operations
- Community infrastructure pilots
- EV charging and transportation projects
- Healthcare access coordination
- Workforce and education programs
- Church, nonprofit, and trust-based community planning
- Strategic planning committees
- Government contracting support

## Quick Start

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Commercialization

Closed Gap Solutions may offer:

- Managed deployment
- Custom configuration
- SBIR/OTA support
- Grant operations support
- Compliance workflow design
- Dashboard integration
- Training and technical assistance
- Enterprise implementation
- Proprietary Sentinel AI Engine extensions

## Data Rights Notice

Public release of this repository does not waive Closed Gap Solutions’ rights in proprietary systems, trade secrets, protected technical data, commercial software, implementation playbooks, or future SBIR/STTR-funded developments.

Any SBIR/STTR-funded technical data or computer software will be marked and handled according to applicable award terms, FAR, DFARS, agency clauses, and SBIR/STTR data-rights requirements.

## Status

This project is currently in MVP/reference-model development.

## License

Apache License 2.0. See `LICENSE`.
