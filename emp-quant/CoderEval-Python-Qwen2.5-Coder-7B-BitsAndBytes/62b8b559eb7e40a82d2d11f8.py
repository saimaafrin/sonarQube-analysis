def minimalBases(classes):
    """
    Returns all classes without subclasses as a list.
    """
    subclasses = {cls: set() for cls in classes}
    
    for cls1, cls2 in classes:
        if cls1 != cls2 and cls2 in classes[cls1]:
            subclasses[cls1].add(cls2)
    
    return [cls for cls, subs in subclasses.items() if not subs]