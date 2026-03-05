def parser_flags(parser):
    return ' '.join([arg.replace('_', '-') for arg in parser._get_all_actions()])