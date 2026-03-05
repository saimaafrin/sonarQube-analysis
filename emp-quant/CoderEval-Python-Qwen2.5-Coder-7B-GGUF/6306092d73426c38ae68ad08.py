def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    List arguments with ``required_when`` condition matched.

    :param command_name: the command name.
    :param options_spec:  the list of command spec options.
    :param args: the received input arguments
    :return: list, list of argument names with matched ``required_when``
        condition
    """
    matched_args = []
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if self._evaluate_condition(condition, args):
                matched_args.append(option['name'])
    return matched_args

def _evaluate_condition(self, condition, args):
    """
    Evaluate the condition for required arguments.

    :param condition: the condition dictionary.
    :param args: the received input arguments
    :return: bool, True if the condition is met, False otherwise
    """
    for key, value in condition.items():
        if key not in args or args[key] != value:
            return False
    return True