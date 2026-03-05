def vertex3tuple(vertices):
# Initialize an empty list to store the result
	result = []
	
	# Iterate over each vertex in the input list
	for i in range(len(vertices)):
		# Get the current vertex
		current_vertex = vertices[i]
		
		# Calculate the indices of the two adjacent vertices
		left_index = (i - 1) % len(vertices)
		right_index = (i + 1) % len(vertices)
		
		# Get the left and right adjacent vertices
		left_vertex = vertices[left_index]
		right_vertex = vertices[right_index]
		
		# Create a tuple with the current vertex and its two adjacent vertices
		tuple_result = (current_vertex, left_vertex, right_vertex)
		
		# Append the tuple to the result list
		result.append(tuple_result)
	
	# Return the final result list
	return result