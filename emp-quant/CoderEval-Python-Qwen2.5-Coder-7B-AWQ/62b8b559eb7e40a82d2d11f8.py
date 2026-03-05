def minimalBases(classes):
    return [c for c in classes if not any(c == s or c in s.__bases__ for s in classes)]