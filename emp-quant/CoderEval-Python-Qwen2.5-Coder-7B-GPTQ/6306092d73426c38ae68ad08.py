def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    List arguments with ``required_when`` condition matched.

    :param command_name: the command name.
    :param options_spec:  the list of command spec options.
    :param args: the received input arguments
    :return: list, list of argument names with matched ``required_when``
        condition
    """
    required_args = []
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if self._evaluate_condition(condition, args):
                required_args.append(option['name'])
    return required_args

def _evaluate_condition(self, condition, args):
    """
    Evaluate a condition based on the provided arguments.

    :param condition: dictionary representing the condition.
    :param args: the received input arguments
    :return: boolean, True if the condition is met, False otherwise
    """
    key = condition['key']
    value = condition['value']
    operator = condition['operator']

    if operator == 'eq':
        return args.get(key) == value
    elif operator == 'ne':
        return args.get(key) != value
    elif operator == 'in':
        return args.get(key) in value
    elif operator == 'notin':
        return args.get(key) not in value
    else:
        raise ValueError(f"Unsupported operator: {operator}")