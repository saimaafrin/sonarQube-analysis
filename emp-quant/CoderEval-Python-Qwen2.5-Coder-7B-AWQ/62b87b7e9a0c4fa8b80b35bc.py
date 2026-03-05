def _update_context(self, context):
    """
    Update *context* with the properties of this graph.

    *context.error* is appended with indices of errors.
    Example subcontext for a graph with fields "E,t,error_E_low":
    {"error": {"x_low": {"index": 2}}}.
    Note that error names are called "x", "y" and "z"
    (this corresponds to first three coordinates,
    if they are present), which allows to simplify plotting.
    Existing values are not removed
    from *context.value* and its subcontexts.

    Called on "destruction" of the graph (for example,
    in :class:`.ToCSV`). By destruction we mean conversion
    to another structure (like text) in the flow.
    The graph object is not really destroyed in this process.
    """
    # Assuming self.properties contains the properties of the graph
    for key, value in self.properties.items():
        if key.startswith('error_'):
            error_type = key[6:]
            if error_type == 'x':
                context.error['x'] = {'index': value}
            elif error_type == 'y':
                context.error['y'] = {'index': value}
            elif error_type == 'z':
                context.error['z'] = {'index': value}
        else:
            context.value[key] = value