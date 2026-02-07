# extractor.py
# import re

# def extract_fields(text):
#     fields = {}

#     policy = re.search(r"POLICY NUMBER[:\s]+(.+)", text, re.I)
#     if policy:
#         fields["policyNumber"] = policy.group(1).strip()

#     date = re.search(r"DATE OF LOSS[:\s]+(.+)", text, re.I)
#     if date:
#         fields["dateOfLoss"] = date.group(1).strip()

#     if "injury" in text.lower():
#         fields["claimType"] = "injury"
#     else:
#         fields["claimType"] = "vehicle"

#     return fields

# extractor.py
import re

def extract_fields(text):
    # 1️⃣ Default structure (required by assessment)
    fields = {
        "policyNumber": "",
        "dateOfLoss": "",
        "insuredName": "",
        "lossLocation": "",
        "injuryInvolved": False,
        "policeReported": False,
        "lossDescription": "",
        "claimType": ""
    }

    # Normalize text
    clean_text = text.replace("\r", "").strip()

    # 2️⃣ Policy Number
    policy = re.search(r"POLICY NUMBER\s*\n\s*([A-Z0-9-]+)", clean_text, re.I)
    if policy:
        fields["policyNumber"] = policy.group(1).strip()

    # 3️⃣ Date of Loss
    date = re.search(r"DATE OF LOSS.*\n\s*([0-9/]+)", clean_text, re.I)
    if date:
        fields["dateOfLoss"] = date.group(1).strip()

    # 4️⃣ Insured Name
    insured = re.search(r"NAME OF INSURED.*\n\s*([A-Z ,]+)", clean_text, re.I)
    if insured:
        fields["insuredName"] = insured.group(1).strip()

    # 5️⃣ Loss Location
    location = re.search(r"LOCATION OF LOSS.*\n\s*(.+)", clean_text, re.I)
    if location:
        fields["lossLocation"] = location.group(1).strip()

    # 6️⃣ Loss Description
    desc = re.search(r"DESCRIPTION OF ACCIDENT.*\n\s*(.+)", clean_text, re.I)
    if desc:
        fields["lossDescription"] = desc.group(1).strip()

    # 7️⃣ Injury Involved
    if "injured" in clean_text.lower() or "bodily injury" in clean_text.lower():
        fields["injuryInvolved"] = True
        fields["claimType"] = "injury"
    else:
        fields["claimType"] = "vehicle"

    # 8️⃣ Police Reported
    if "police" in clean_text.lower() or "fire department" in clean_text.lower():
        fields["policeReported"] = True

    return fields
