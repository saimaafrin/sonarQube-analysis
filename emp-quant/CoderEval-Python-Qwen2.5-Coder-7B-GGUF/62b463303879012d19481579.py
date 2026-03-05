def _extract_number_and_supplement_from_issue_element(issue):
    number = None
    sup = None
    if isinstance(issue, str):
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = int(part)
            elif part.isalpha():
                sup = part
    return number, sup