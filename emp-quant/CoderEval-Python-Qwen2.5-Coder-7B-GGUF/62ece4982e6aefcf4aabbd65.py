def parser_flags(parser):
    return ' '.join([f'--{flag}' for flag in parser._actions if flag.dest != 'help'])