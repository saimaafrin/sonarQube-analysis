def get_deprecated_args(self):
    deprecated_args = {}
    for option_spec in self.spec_helper.iterate_option_specs():
        if option_spec.deprecated:
            deprecated_args[option_spec.name] = option_spec.deprecates
    return deprecated_args