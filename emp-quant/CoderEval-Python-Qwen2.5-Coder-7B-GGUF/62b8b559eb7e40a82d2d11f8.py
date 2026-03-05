def minimalBases(classes):
    subclasses = set()
    for cls in classes:
        for subclass in classes:
            if cls != subclass and issubclass(subclass, cls):
                subclasses.add(cls)
    return [cls for cls in classes if cls not in subclasses]