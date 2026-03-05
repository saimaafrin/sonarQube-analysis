def paging(response, max_results):
# Check if the response is a list and not empty
	if isinstance(response, list) and len(response) > 0:
		# Calculate the total number of pages needed
		total_pages = (len(response) + max_results - 1) // max_results
		# Iterate over each page
		for i in range(total_pages):
			# Yield the current page's slice of the response
			yield response[i * max_results:(i + 1) * max_results]
	else:
		# If the response is not a list or is empty, yield it as is
		yield response