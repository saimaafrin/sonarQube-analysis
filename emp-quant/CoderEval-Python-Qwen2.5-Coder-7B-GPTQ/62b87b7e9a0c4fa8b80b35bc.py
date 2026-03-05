def _update_context(self, context):
    if 'error' not in context:
        context['error'] = {}
    
    for field in self.fields:
        if 'error_' + field in self.errors:
            error_index = self.errors['error_' + field]
            if field[:3] == 'xyz':
                axis = {'x': 0, 'y': 1, 'z': 2}.get(field[3:], None)
                if axis is not None:
                    if axis not in context['error']:
                        context['error'][axis] = {}
                    context['error'][axis]['index'] = error_index
            else:
                if field not in context['error']:
                    context['error'][field] = {}
                context['error'][field]['index'] = error_index
    
    return context