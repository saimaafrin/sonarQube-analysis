def pop_u16(self):
    """
    Remove the last two elements in self.data and return
    """
    if len(self.data) >= 2:
        return self.data.pop() & 0xFFFF
    else:
        raise IndexError("pop from an empty array")