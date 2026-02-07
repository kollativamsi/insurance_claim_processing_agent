# router.py

MANDATORY_FIELDS = ["policyNumber", "claimType"]

def find_missing(fields):
    return [f for f in MANDATORY_FIELDS if f not in fields]

# def route_claim(fields, missing, text):
#     if missing:
#         return "Manual Review", "Mandatory fields missing"

#     if "fraud" in text.lower() or "staged" in text.lower():
#         return "Investigation", "Suspicious keywords detected"

#     if fields.get("claimType") == "injury":
#         return "Specialist Queue", "Injury related claim"

#     return "Manual Review", "Default routing"

def route_claim(fields, missing, invalid, text):

    if missing or invalid:
        return "Manual Review", "Missing or inconsistent FNOL data"

    if "staged accident" in text.lower():
        return "Investigation", "Suspicious claim description"

    if fields.get("claimType") == "injury":
        return "Specialist Queue", "Injury-related claim"

    return "Manual Review", "Default routing"



# def find_missing_and_invalid(fields):
#     missing = []
#     invalid = []

#     for key, value in fields.items():
#         if value == "" or value is None:
#             missing.append(key)

#         # Detect placeholder junk from ACORD templates
#         elif value.isupper() and len(value.split()) <= 3:
#             invalid.append(key)

#     return missing, invalid

def find_missing_and_invalid(fields):
    missing = []
    invalid = []

    for key, value in fields.items():
        # Missing value check
        if value == "" or value is None:
            missing.append(key)

        # Invalid placeholder text (ONLY for strings)
        elif isinstance(value, str):
            if value.isupper() and len(value.split()) <= 3:
                invalid.append(key)

    return missing, invalid

