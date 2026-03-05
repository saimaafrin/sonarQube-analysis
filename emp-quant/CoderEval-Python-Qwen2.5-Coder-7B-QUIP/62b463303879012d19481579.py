def _extract_number_and_supplment_from_issue_element(issue):
    number = None
    suppl = None

    # Assuming issue is a string and contains the number and suppl information
    # Example format: "issue-12345-sup-a"
    parts = issue.split('-')
    if len(parts) > 2:
        number = parts[1]
        suppl = parts[2]

    return number, suppl