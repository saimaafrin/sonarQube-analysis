def _update_context(self, context):
    if 'error' not in context:
        context['error'] = {}
    
    for field in self.fields:
        if field.startswith('error_'):
            error_type = field[6:]
            if error_type == 'x':
                index = self.get_error_index(error_type)
                if index is not None:
                    context['error'].setdefault('x', []).append(index)
            elif error_type == 'y':
                index = self.get_error_index(error_type)
                if index is not None:
                    context['error'].setdefault('y', []).append(index)
            elif error_type == 'z':
                index = self.get_error_index(error_type)
                if index is not None:
                    context['error'].setdefault('z', []).append(index)

    return context