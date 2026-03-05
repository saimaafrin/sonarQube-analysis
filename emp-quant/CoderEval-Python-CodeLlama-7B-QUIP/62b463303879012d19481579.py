def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	sup = None
	if issue.contents:
		for content in issue.contents:
			if content.tag == 'span':
				if content.contents[0].text.strip() == 'Supplement':
					sup = content.contents[1].text.strip()
				else:
					number = content.contents[0].text.strip()
	return number, sup