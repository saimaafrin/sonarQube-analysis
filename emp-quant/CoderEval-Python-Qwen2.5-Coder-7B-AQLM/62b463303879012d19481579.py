def _extract_number_and_supplement_from_issue_element(issue):
    """
    Return the possible values of number and sup from the contents of issue.
    """
    number = None
    sup = None
    if isinstance(issue, str):
        parts = issue.split()
        for part in parts:
            if part.isdigit():
                number = int(part)
            elif part.isalpha() and part.isupper():
                sup = part
    return number, sup