def minimalBases(classes):
# Create a dictionary to store the parent of each class
	parents = {}
	for cls in classes:
		if cls[1] != -1:  # If the class has a parent
			parents[cls[0]] = cls[1]

	# Find all classes that are not subclasses of any other class
	minimal_classes = []
	for cls in classes:
		if cls[0] not in parents.values():  # If the class is not a subclass
			minimal_classes.append(cls)

	return minimal_classes

classes = [
    (1, -1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3)
]
print(minimalBases(classes))  # Output: [(1, -1), (4, 2), (5, 3)]