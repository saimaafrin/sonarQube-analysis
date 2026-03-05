self.context = {}
for bin_name in self.bins:
    if hasattr(self, f"_{bin_name}_initial_value"):
        setattr(self, bin_name, getattr(self, f"_{bin_name}_initial_value"))
    else:
        setattr(self, bin_name, self.make_bins())