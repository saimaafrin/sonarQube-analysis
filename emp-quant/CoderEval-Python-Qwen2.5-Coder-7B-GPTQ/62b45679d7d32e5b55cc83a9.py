def parser_flags(parser):
    return ' '.join([f'--{flag}' for flag in dir(parser) if not callable(getattr(parser, flag)) and not flag.startswith('_')])