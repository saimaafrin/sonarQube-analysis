import argparse

def parse_arguments(*arguments):
    parser = argparse.ArgumentParser(description='Parse command-line arguments')
    for arg in arguments:
        parser.add_argument(arg, help=f'Argument {arg}')
    return parser