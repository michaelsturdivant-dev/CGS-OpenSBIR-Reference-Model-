# CGS Secrets Setup Guide

Do not paste live secrets into chat, issues, pull requests, commits, README files, screenshots, or public documentation.

## GitHub Repository Secrets

GitHub repo → Settings → Secrets and variables → Actions → Secrets → New repository secret.

Add the following names exactly:

- MAKE_WEBHOOK_URL
- NETLIFY_AUTH_TOKEN
- NETLIFY_SITE_ID
- STRIPE_SECRET_KEY
- STRIPE_WEBHOOK_SECRET
- SQUARE_ACCESS_TOKEN
- SQUARE_WEBHOOK_SIGNATURE_KEY
- SQUARE_LOCATION_ID
- CHERRY_PUBLIC_KEY or approved Cherry credential name
- CHERRY_PRIVATE_KEY or approved Cherry credential name

## Gate Rules

Gate 4 is required before public checkout/payment pages go live.

Gate 5 is required before live payments, financing, subscriptions, refunds, invoices, paid APIs, or gateway activation.

## Validation

After secrets are added, run GitHub Actions workflow: CGS Make and Netlify Dispatch.

Start with notify_make true, deploy_to_netlify false, and cgs_gate set to Gate 5 approved for test-mode secret validation only.
