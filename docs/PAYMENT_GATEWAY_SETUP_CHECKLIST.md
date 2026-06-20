# CGS Payment Gateway Setup Checklist

## Gate 5 Financial Clearance

- [ ] Stripe account verified
- [ ] Square account verified
- [ ] Affirm enabled in Stripe only if eligible
- [ ] Cherry merchant/partner access verified
- [ ] Test mode separated from live mode
- [ ] Gateway secrets stored in GitHub secrets, Netlify environment variables, or approved platform vault
- [ ] No payment secrets committed to repository
- [ ] Webhook endpoint tested
- [ ] Refund path tested
- [ ] Evidence record updated

## GitHub Secrets

- STRIPE_SECRET_KEY
- STRIPE_WEBHOOK_SECRET
- SQUARE_ACCESS_TOKEN
- SQUARE_WEBHOOK_SIGNATURE_KEY
- SQUARE_LOCATION_ID
- CHERRY_PUBLIC_KEY or approved credential name
- CHERRY_PRIVATE_KEY or approved credential name

## Netlify Environment Variables

Mirror only the required production variables after Gate 5 approval.

## Make.com

Make.com may receive payment events for notification or registry update only. It may not approve, refund, deploy, finance, or change pricing.

## Gate 4 Release

No payment button, checkout page, financing page, or public checkout URL may go live without Gate 4 release approval.
