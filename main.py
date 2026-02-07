# main.py
import json
from utils import read_pdf, read_txt
from extractor import extract_fields
from router import route_claim, find_missing_and_invalid
# choose input file
file_path = "samples/fnol1.pdf"

if file_path.endswith(".pdf"):
    text = read_pdf(file_path)
else:
    text = read_txt(file_path)

fields = extract_fields(text)
missing, invalid = find_missing_and_invalid(fields)
route, reason = route_claim(fields, missing,invalid, text)

output = {
    "extractedFields": fields,
    "missingFields": missing,
    "invalidFields": invalid,
    "recommendedRoute": route,
    "reasoning": reason
}

print(json.dumps(output, indent=2))
text = read_pdf(file_path)
print(text[:1000])   #temporary debug


