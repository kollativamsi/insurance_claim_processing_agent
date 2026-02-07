Autonomous Insurance Claims Processing Agent
Overview

This project is a lightweight rule-based insurance claims processing agent.
It processes FNOL (First Notice of Loss) documents in PDF or TXT format, extracts key claim information, validates the data quality, and recommends the correct processing route.

The goal of this agent is accuracy, explainability, and safe routing, not machine learning.

Problem Statement

Insurance FNOL documents often:

Contain missing information

Contain unfilled template labels instead of real values

Vary in structure (PDF / TXT)

This agent addresses those challenges by:

Extracting available fields

Detecting missing and inconsistent data

Routing claims safely using deterministic rules

Providing a clear explanation for every routing decision

Project Structure
insurance_agent/
│
├── main.py          # Entry point – orchestrates the full flow
├── extractor.py     # FNOL field extraction logic
├── router.py        # Validation + routing rules
├── utils.py         # PDF / TXT file reading helpers
│
├── samples/         # Sample FNOL input files
│     ├── fnol1.txt
│     └── ACORD-Automobile-Loss-Notice.pdf
│
└── README.md

Processing Flow (High Level)
FNOL PDF / TXT
     ↓
Text Extraction
     ↓
Field Extraction
     ↓
Missing & Invalid Field Detection
     ↓
Routing Decision
     ↓
JSON Output

Fields Extracted

The agent attempts to extract the following FNOL fields:

Policy Number

Date of Loss

Insured Name

Loss Location

Loss Description

Injury Involved (True / False)

Police Reported (True / False)

Claim Type (injury / vehicle)

If a field cannot be reliably extracted, it is left empty and handled by validation logic.

Data Validation Logic

The agent does both presence and quality validation:

Missing Fields

A field is marked missing if:

It is empty ("")

It is not found in the document

Invalid Fields

A field is marked invalid if:

It contains placeholder template text
(e.g., CONTACT, STREET, INSURED VEHICLE)

It looks like an unfilled ACORD form label rather than real data

This is important because ACORD PDFs often include labels even when values are not filled.

Routing Rules

Routing decisions are rule-based and explainable:

Condition	Route
Missing or invalid FNOL data	Manual Review
Claim type = injury	Specialist Queue
Suspicious phrases like “staged accident”	Investigation
Default fallback	Manual Review

The agent intentionally avoids using generic “fraud” keywords because ACORD forms always include fraud disclaimers.

Output Format

The final output is a structured JSON object:

{
  "extractedFields": {},
  "missingFields": [],
  "invalidFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}


Every routing decision includes a human-readable explanation.

Handling ACORD PDFs

ACORD FNOL PDFs are template-based.

If the form is unfilled:

Label text may appear as extracted values

The agent detects such cases as invalid fields

The claim is routed to Manual Review for safety

This behavior is intentional and correct.

How to Run the Project
Prerequisites

Python 3.x

pdfplumber library

Install dependency:

pip install pdfplumber

Run
python main.py

Input Selection

Update the file path in main.py:

file_path = "samples/fnol1.txt"
# or
file_path = "samples/ACORD-Automobile-Loss-Notice.pdf"

Design Decisions

No machine learning → deterministic and explainable behavior

Rule-based routing → safer for critical insurance workflows

Explicit validation → avoids false confidence in bad data

Simple modular structure → easy to extend and review

Limitations & Future Improvements

Scanned PDFs (image-only) are not supported (OCR can be added)

Regex-based extraction may miss some fields in complex layouts

Additional routing rules can be added for commercial or high-value claims

Conclusion

This project demonstrates:

Real-world FNOL handling

Data quality awareness

Safe claim routing decisions

Clean, maintainable Python design

The agent prioritizes correctness and explainability, which are critical in insurance workflows.
