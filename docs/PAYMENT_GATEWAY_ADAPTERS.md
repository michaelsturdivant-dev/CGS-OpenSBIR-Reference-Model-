# CGS Payment Gateway Adapter Doctrine

Owner: Closed Gap Solutions LLC / Michael Sturdivant
System: CGS CUBE-EAGLE
Status: Draft pending Gate 5 financial clearance

## Purpose

This document incorporates Stripe, Square, Affirm, and Cherry as payment or financing adapters under the CGS external adapter model.

## Master Rule

CUBE-EAGLE may use SaaS. SaaS may not use CUBE-EAGLE.

## Payment Rail Positioning

1. Stripe is the primary online checkout and payment-link rail.
2. Square is the secondary point-of-sale, invoice, card-present, and alternate online payment rail.
3. Affirm is a buy-now-pay-later financing option enabled through Stripe where eligible.
4. Cherry is a separate patient/client financing adapter until official API credentials, merchant agreement, and compliance rules are verified.

## Gates

Gate 5 is required before live payments, financing, refunds, subscriptions, invoices, paid API activation, or production payment-link release.

Gate 4 is required before any payment page, checkout URL, financing offer page, landing page, or payment button is published externally.

## Required Secrets

- STRIPE_SECRET_KEY
- STRIPE_WEBHOOK_SECRET
- SQUARE_ACCESS_TOKEN
- SQUARE_WEBHOOK_SIGNATURE_KEY
- SQUARE_LOCATION_ID
- CHERRY_PUBLIC_KEY or approved Cherry credential name
- CHERRY_PRIVATE_KEY or approved Cherry credential name

## Evidence Required

Each live gateway must have merchant confirmation, secret setup confirmation, test transaction record, webhook verification record, refund test record, checkout approval record, Gate 4 release approval, Gate 5 financial clearance, and evidence folder link.

## Standing Payment Rule

Stripe, Square, Affirm, and Cherry are adapters. They may collect or finance approved payments. They may not define CGS authority, pricing doctrine, client eligibility, protected backend logic, or release clearance.
