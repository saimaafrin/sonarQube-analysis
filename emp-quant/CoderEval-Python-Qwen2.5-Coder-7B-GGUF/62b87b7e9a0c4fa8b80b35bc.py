def _update_context(self, context):
    if not hasattr(context, 'error'):
        context.error = {}
    if not hasattr(context, 'value'):
        context.value = {}

    for field in self.fields:
        if field.startswith('error_'):
            error_type = field[6:]
            if error_type not in context.error:
                context.error[error_type] = {}
            context.error[error_type]['index'] = self.get_error_index(error_type)

    for field in self.fields:
        if field not in context.value:
            context.value[field] = self.get_field_value(field)