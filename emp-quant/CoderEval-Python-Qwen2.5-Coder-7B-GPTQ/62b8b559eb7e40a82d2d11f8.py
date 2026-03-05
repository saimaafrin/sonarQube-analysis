def minimalBases(classes):
    """
    Returns all classes without subclasses as a list.
    """
    subclasses = set()
    for cls in classes:
        for subcls in classes:
            if cls != subcls and issubclass(subcls, cls):
                subclasses.add(cls)
    return [cls for cls in classes if cls not in subclasses]