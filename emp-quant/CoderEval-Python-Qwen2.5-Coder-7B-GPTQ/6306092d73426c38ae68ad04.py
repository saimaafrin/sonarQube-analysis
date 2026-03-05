import argparse

class CommandParser:
    def __init__(self):
        self.parsers = {
            'main': argparse.ArgumentParser(description='Main command'),
            'virsh': argparse.ArgumentParser(description='Virsh command'),
            'ospd': argparse.ArgumentParser(description='Ospd command')
        }
        self.setup_options()

    def setup_options(self):
        self.parsers['main'].add_argument('--option1', help='Option 1 for main')
        self.parsers['main'].add_argument('--option2', help='Option 2 for main')

        self.parsers['virsh'].add_argument('--vm', help='Virtual Machine name')
        self.parsers['virsh'].add_argument('--action', help='Action to perform on VM')

        self.parsers['ospd'].add_argument('--port', type=int, help='Port number for OSPD')

    def get_parser_option_specs(self, command_name):
        return self.parsers[command_name].get_all_actions()