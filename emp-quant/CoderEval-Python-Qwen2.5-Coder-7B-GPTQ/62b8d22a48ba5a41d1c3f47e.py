if key in self:
    return self[key]
else:
    self[key] = default
    return default