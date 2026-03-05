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
    for key, value in self._get_properties().items():
        if key == 'error':
            if 'error' not in context:
                context.error = {}
            for subkey, subvalue in value.items():
                if subkey not in context.error:
                    context.error[subkey] = {}
                context.error[subkey]['index'] = subvalue
        else:
            if key not in context:
                context[key] = value
            else:
                context[key] = value