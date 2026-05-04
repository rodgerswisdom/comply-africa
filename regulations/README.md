# Regulations

Structured regulatory documents for African financial compliance.

## Directory Structure

```
regulations/
├── kenya/
│   ├── cbk/          # Central Bank of Kenya
│   ├── fatf/         # FATF evaluations
│   └── cma/          # Capital Markets Authority
├── nigeria/
│   └── cbn/          # Central Bank of Nigeria
└── ghana/
    └── bog/          # Bank of Ghana
```

## File Format

Each regulation is a JSON file with:
- `document_metadata`: ID, title, type, issuer, dates
- `extracted_obligations`: Machine-readable compliance requirements
- `obligations_for_institutions`: Mapping to specific institution types
- `penalties`: Consequences of non-compliance
- `data_quality`: Extraction confidence and verification status

## Adding a New Regulation

1. Place PDF in `raw/` directory
2. Run extraction: `python scripts/extract_regulation.py --file raw/circular.pdf --country KE --regulator CBK`
3. Review and verify the JSON output
4. Update `data_quality.confidence` to "high" after verification
5. Run validation: `python scripts/validate.py regulations/kenya/cbk/*.json`
6. Update `index.json`
7. Commit

## Verification Status

| Status | Meaning | Can Use? |
|--------|---------|----------|
| `needs_manual_review` | Automated extraction, not verified | ❌ No |
| `pending_review` | Human reviewed, needs second pair of eyes | ⚠️ Caution |
| `verified` | Multiple reviewers confirmed | ✅ Yes |

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
