def minimalBases(classes):
    return [cls for cls in classes if not any(issubclass(cls, base) for base in classes if base != cls)]