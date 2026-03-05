def _extract_number_and_supplment_from_issue_element(issue):
# Extract the number and supplement from the issue element
	number = issue.get('number')
	supplement = issue.get('supplement')

	return number, supplement