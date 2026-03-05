def paging(response, max_results):
	"""
	Return every response with the length of max_results
    Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.
	"""
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max_results > 100:
		raise ValueError("max_results must be less than 100")
	if max_results <= 0:
		raise ValueError("max_results must be greater than 0")
	if max_results < 1:
		raise ValueError("max_results must be greater than 0")
	if max