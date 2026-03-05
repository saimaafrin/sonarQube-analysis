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
    if not hasattr(context, 'error'):
        context.error = {}

    for field in self.fields:
        if field.startswith('error_'):
            error_type = field[6:]
            if error_type in ['x', 'y', 'z']:
                index = getattr(self, error_type + '_low')
                if index is not None:
                    if error_type not in context.error:
                        context.error[error_type] = {}
                    context.error[error_type]['index'] = index