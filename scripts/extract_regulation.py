#!/usr/bin/env python3
"""
ComplyAfrica Regulation Extractor
Usage: python extract_regulation.py --file /path/to/pdf --type mer --country KE --regulator CBK
"""

import argparse
import json
import PyPDF2
from datetime import datetime
import os
import re

def extract_from_pdf(pdf_path):
    """Extract text from PDF"""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def identify_document_type(text):
    """Identify if it's MER, Guideline, Circular, etc."""
    text_lower = text.lower()
    if "mutual evaluation" in text_lower:
        return "mutual_evaluation_report"
    elif "guideline" in text_lower:
        return "guideline"
    elif "circular" in text_lower:
        return "circular"
    elif "directive" in text_lower:
        return "directive"
    return "unknown"

def extract_obligations(text, doc_type):
    """Extract obligations based on document type"""
    obligations = []

    if doc_type == "mutual_evaluation_report":
        # Look for FATF Recommendation references
        r_pattern = r'Recommendation\s+(\d+)\s*[-\u2013]\s*([^\n]+)'
        matches = re.findall(r_pattern, text)

        for match in matches:
            r_num, r_title = match
            obligations.append({
                "obligation_id": f"r{r_num}",
                "source_r": f"r_{r_num}",
                "title": r_title.strip(),
                "text": "Extracted from MER - full text needs manual review",
                "applies_to": [],
                "implementation_status": "unknown",
                "priority": "medium",
                "deadline": "unknown"
            })

    return obligations

def create_regulation_json(pdf_path, country, regulator):
    """Main extraction workflow"""
    text = extract_from_pdf(pdf_path)
    doc_type = identify_document_type(text)

    # Create metadata
    doc_id = f"{regulator.lower()}-{doc_type.replace('_', '-')}-{country.lower()}-{datetime.now().year}"

    regulation = {
        "document_metadata": {
            "id": doc_id,
            "title": os.path.basename(pdf_path).replace('.pdf', ''),
            "document_type": doc_type,
            "issuing_body": regulator,
            "assessed_country": country,
            "publication_date": datetime.now().strftime("%Y-%m-%d"),
            "url": "",
            "extraction_method": "automated_pdf"
        },
        "extracted_obligations": extract_obligations(text, doc_type),
        "raw_text_sample": text[:5000],  # First 5000 chars for manual review
        "data_quality": {
            "extraction_date": datetime.now().isoformat(),
            "extracted_by": "automated_script",
            "confidence": "low",
            "verification_status": "needs_manual_review",
            "notes": "Automated extraction. Requires human verification before use."
        }
    }

    return regulation

def main():
    parser = argparse.ArgumentParser(description='Extract regulations from PDF')
    parser.add_argument('--file', required=True, help='Path to PDF file')
    parser.add_argument('--country', required=True, help='Country code (e.g., KE, NG, GH)')
    parser.add_argument('--regulator', required=True, help='Regulator code (e.g., CBK, CBN, BOG)')
    parser.add_argument('--output', help='Output directory', default='regulations')

    args = parser.parse_args()

    # Extract
    regulation = create_regulation_json(args.file, args.country, args.regulator)

    # Save
    output_dir = f"{args.output}/{args.country.lower()}/{args.regulator.lower()}"
    os.makedirs(output_dir, exist_ok=True)

    output_file = f"{output_dir}/{regulation['document_metadata']['id']}.json"
    with open(output_file, 'w') as f:
        json.dump(regulation, f, indent=2)

    print(f"✅ Extracted: {output_file}")
    print(f"⚠️  WARNING: This is automated extraction. Manual review REQUIRED.")
    print(f"📋 Next steps:")
    print(f"   1. Review extracted obligations")
    print(f"   2. Verify document metadata")
    print(f"   3. Update 'confidence' to 'high' after verification")
    print(f"   4. Commit to git when verified")

if __name__ == "__main__":
    main()
