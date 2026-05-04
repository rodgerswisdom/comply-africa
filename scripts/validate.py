#!/usr/bin/env python3
"""
Validate regulation JSON against schema
Usage: python validate.py regulations/kenya/cbk/*.json
"""

import json
import sys
import glob
from pathlib import Path

def validate_regulation(file_path):
    """Validate a single regulation file"""
    with open(file_path) as f:
        data = json.load(f)

    errors = []

    # Check required fields
    if "document_metadata" not in data:
        errors.append("Missing document_metadata")
    else:
        meta = data["document_metadata"]
        required_meta = ["id", "title", "document_type", "issuing_body", "assessed_country", "publication_date"]
        for field in required_meta:
            if field not in meta:
                errors.append(f"Missing metadata field: {field}")

    if "extracted_obligations" not in data:
        errors.append("Missing extracted_obligations")
    elif not isinstance(data["extracted_obligations"], list):
        errors.append("extracted_obligations must be an array")

    # Check data quality
    if "data_quality" in data:
        dq = data["data_quality"]
        if dq.get("confidence") == "low":
            errors.append("WARNING: Low confidence - needs manual review")
        if dq.get("verification_status") == "needs_manual_review":
            errors.append("WARNING: Not verified - do not use in production")

    return errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate.py <glob_pattern>")
        sys.exit(1)

    pattern = sys.argv[1]
    files = glob.glob(pattern)

    if not files:
        print(f"No files found matching: {pattern}")
        sys.exit(1)

    total_errors = 0
    for file_path in files:
        errors = validate_regulation(file_path)
        if errors:
            print(f"
❌ {file_path}:")
            for error in errors:
                print(f"   - {error}")
            total_errors += len(errors)
        else:
            print(f"✅ {file_path}")

    print(f"
{'='*50}")
    print(f"Files checked: {len(files)}")
    print(f"Errors found: {total_errors}")

    if total_errors > 0:
        print("
⚠️  Fix errors before committing!")
        sys.exit(1)
    else:
        print("
🎉 All files valid!")

if __name__ == "__main__":
    main()
