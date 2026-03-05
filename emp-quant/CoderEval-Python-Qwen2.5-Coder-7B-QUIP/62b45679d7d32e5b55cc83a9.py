def parser_flags(parser):
    return ' '.join([flag.lstrip('-') for flag in parser._get_all_parseractions()])