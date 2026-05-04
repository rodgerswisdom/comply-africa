# Quick Reference: Working with Regulations

## Extract from PDF
```bash
python scripts/extract_regulation.py \
    --file raw/cbk-circular-2024-01.pdf \
    --country KE \
    --regulator CBK \
    --output regulations
```

## Validate All Files
```bash
python scripts/validate.py "regulations/**/*.json"
```

## Check Index
```bash
cat index.json | jq '.regulations[] | {id, status, confidence}'
```

## Find Obligations for Your Institution
```bash
jq '.extracted_obligations[] | select(.applies_to | contains(["microfinance_banks"]))' \
    regulations/kenya/fatf/fatf-mer-kenya-2022.json
```

## Find High Priority Obligations
```bash
jq '.extracted_obligations[] | select(.priority == "high")' \
    regulations/kenya/fatf/fatf-mer-kenya-2022.json
```
