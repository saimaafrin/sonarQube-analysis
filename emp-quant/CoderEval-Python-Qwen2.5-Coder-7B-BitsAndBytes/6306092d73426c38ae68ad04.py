import argparse

class CommandParser:
    def __init__(self):
        self.parsers = {
            'main': argparse.ArgumentParser(description='Main command'),
            'virsh': argparse.ArgumentParser(description='Virsh command'),
            'ospd': argparse.ArgumentParser(description='Ospd command')
        }

    def add_options(self, parser, options):
        for option in options:
            parser.add_argument(*option['args'], **option['kwargs'])

    def get_parser_option_specs(self, command_name):
        if command_name not in self.parsers:
            raise ValueError(f"Command '{command_name}' not found")
        
        parser = self.parsers[command_name]
        return [(action.dest, action.default) for action in parser._actions]