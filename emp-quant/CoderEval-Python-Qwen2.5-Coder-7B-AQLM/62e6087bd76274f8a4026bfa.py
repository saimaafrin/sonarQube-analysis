def pop_u16(self):
    """
    Remove the last two elements in self.data and return
    """
    return self.data.pop() & 0xFFFF, self.data.pop() & 0xFFFF