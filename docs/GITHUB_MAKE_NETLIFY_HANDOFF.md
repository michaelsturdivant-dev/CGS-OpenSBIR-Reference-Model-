# GitHub to Make.com to Netlify Handoff

Required GitHub repository secrets:

- MAKE_WEBHOOK_URL
- NETLIFY_AUTH_TOKEN
- NETLIFY_SITE_ID

Make.com is a webhook relay only. It may receive GitHub dispatch events, create task records, notify stakeholders, or update non-authority registries.

Make.com may not approve release, deploy production, spend money, submit grants, represent CGS, alter protected repository files, or bypass human clearance.

Netlify is a static deployment shell only. Production deployment requires Gate 4 approval.

Use GitHub Actions workflow `CGS Make and Netlify Dispatch`.

Set notify_make to true. Set deploy_to_netlify to false unless Gate 4 is approved. Set cgs_gate to include approved only after human clearance.

CUBE-EAGLE may use SaaS. SaaS may not use CUBE-EAGLE.
