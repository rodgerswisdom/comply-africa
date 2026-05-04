# Contributing to ComplyAfrica

## How to Contribute Regulations

### Option 1: Submit a PDF
1. Open a GitHub issue with title: `[REGULATION] Country: Regulator: Topic`
2. Attach or link the PDF
3. We'll extract and structure it

### Option 2: Submit Structured Data
1. Fork the repo
2. Create JSON following the schema in `schemas/regulation_schema.json`
3. Run `python scripts/validate.py` on your file
4. Submit PR

### Option 3: Verify Existing Data
1. Find a regulation marked `confidence: low` or `verification_status: needs_manual_review`
2. Review against original PDF
3. Update fields and change status to `verified`
4. Submit PR

## Data Quality Standards

- **High confidence**: You have read the original document and confirmed all fields
- **Medium confidence**: Automated extraction, you spot-checked key fields
- **Low confidence**: Automated extraction, needs human review

## Institution Type Codes

| Code | Description |
|------|-------------|
| `commercial_banks` | Licensed commercial banks |
| `microfinance_banks` | Microfinance banks |
| `forex_bureaus` | Foreign exchange bureaus |
| `mobile_money_operators` | Mobile money providers (M-Pesa, etc.) |
| `dnfbps` | Designated non-financial businesses and professions |
| `insurance` | Insurance companies |
| `securities` | Capital markets intermediaries |

## Priority Levels

| Level | Description |
|-------|-------------|
| `critical` | Immediate compliance risk, regulator enforcement action likely |
| `high` | Required by law, deadline approaching |
| `medium` | Best practice, regulatory expectation |
| `low` | Guidance, recommended but not mandatory |

## Contact

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Email: rodgers@keverd.com
