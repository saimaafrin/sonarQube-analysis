import sys
from configparser import ConfigParser
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'
def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Add the path to sys.path
    sys.path.append(path_to_append)
    # Create a new ConfigParser object
    config = ConfigParser()
    # Read the configuration file
    config.read(config_file)
    # Update the configuration file
    config.set('section', 'key', 'value')
    # Write the updated configuration to the file
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    # Return the updated configuration object and the path to the configuration file
    return config, config_file