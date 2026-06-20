# CGS CUBE-EAGLE™ Terms of Reference

**Owner / Architect:** Michael Sturdivant  
**Entity:** Closed Gap Solutions LLC  
**System:** CGS CUBE-EAGLE™ Master Backend Synergy Application  
**Doctrine:** Adapter, Not Authority™  
**Authority Rule:** Autonomous in preparation, human-cleared in authority  
**Applied To:** This repository and all related architectures, code, APIs, webhooks, databases, schemas, deployment adapters, and evidence controls.

## Master Rule

**CUBE-EAGLE may use SaaS. SaaS may not use CUBE-EAGLE.**

## Purpose

This Terms of Reference governs how this repository participates in the CGS ecosystem. It applies to repository structure, architecture decisions, code, authentic APIs, webhooks, databases, schemas, adapter integrations, deployment shells, evidence logs, and external release decisions.

## Governing Principles

1. Human authority remains supreme.
2. AI may prepare, classify, route, draft, and recommend.
3. AI may not release, submit, spend, deploy, represent, or bind CGS without clearance.
4. SaaS is an adapter, not authority.
5. GitHub is the technical source of truth.
6. Google Drive is the evidence and document store.
7. No secrets are stored in code.
8. Every external adapter must declare role, scope, action, and clearance status.
9. Every artifact must be traceable to requirement, authority, evidence, and next action.
10. Every production or external-facing action requires a human clearance gate.

## Cube Method Requirement

Every project, API, schema, webhook, database, architecture, or code artifact must be classified by Mission, Requirement, Authority, Execution, Evidence, and Value.

Nothing exits the Cube until it has a CGS lane, authority basis, human gate, evidence expectation, target adapter, risk level, next action, and registry disposition.

## Human Clearance Gates

Gate 0 — Registry Acceptance.  
Gate 1 — Requirement Authority.  
Gate 2 — Funding / Eligibility / Representation.  
Gate 3 — Build Authorization.  
Gate 4 — External Release.  
Gate 5 — Financial Commitment.  
Gate 6 — Evidence Lock.  
Gate 7 — L2KM Integration.

No external action may bypass these gates.

## Repository Requirements

This repository must maintain a README, ownership notice, `.env.example`, documentation folder, evidence folder where applicable, release notes, approval record, schema folder where applicable, adapter folder where applicable, deployment notes, and protected backend boundary statement.

## API and Webhook Requirements

Every API or webhook must define endpoint, purpose, owner, authentication method, allowed callers, request schema, response schema, required human gate, data sensitivity, logging requirement, evidence record, deactivation process, and cost exposure if any.

Every webhook payload must include event_type, source_system, project_id, requested_action, title, target_adapter, adapter_role, human_gate_required, clearance_status, risk_level, evidence_required, doctrine_acknowledged, and timestamp.

## Database and Schema Requirements

Every database, table, registry, sheet, or structured store must define owner, edit authority, backup requirement, export method, retention status, sensitive fields, audit requirements, approved integrations, deletion/archive rules, and evidence linkage.

Every schema must include name, version, owner, purpose, required fields, optional fields, validation rules, data sensitivity, approved source systems, approved target systems, human gate, example payload, and change log.

## Security and Secrets

No CGS system may expose API keys, OAuth tokens, passwords, secrets, client-sensitive data, protected backend prompts, private schemas, non-public strategy, confidential pricing, proprietary scoring logic, or internal route logic.

Live secrets must be stored only in approved secret managers or secure environment-variable systems.

## External Adapter Rule

External systems may connect only as adapters. Reject or block any adapter that attempts to become authority, claims CGS IP, bypasses clearance, locks data without export, stores secrets insecurely, hides workflow logic, charges without approval, triggers unapproved automation, exposes protected backend architecture, or cannot produce evidence.

## Evidence Requirements

Every repository, architecture, API, webhook, database, schema, and code artifact must produce approval records, decision logs, test logs, release notes, risk notes, evidence location, and L2KM lessons where applicable.

## IP Notice

© 2026 Closed Gap Solutions LLC. All rights reserved. Created by Michael Sturdivant. Protected CGS intellectual property.

## Standing Command

Protect CGS IP. Preserve human authority. Classify through the Cube Method. Assign a human clearance gate. Keep SaaS as adapter only. Record evidence. Route to GitHub or Drive. Deploy only after clearance. Capture L2KM. Keep the backend inside the box.
