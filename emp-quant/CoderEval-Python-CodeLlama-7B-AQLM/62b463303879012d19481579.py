def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	sup = None
	if issue.text:
		number = issue.text
		if issue.get('suppl'):
			sup = issue.get('suppl')
	return number, sup