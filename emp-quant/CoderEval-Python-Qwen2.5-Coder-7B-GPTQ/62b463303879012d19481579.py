import re

def _extract_number_and_supplement_from_issue_element(issue):
    match = re.search(r'(\d+)([A-Za-z]*)', issue)
    if match:
        number = int(match.group(1))
        supplement = match.group(2)
        return number, supplement
    else:
        return None, None