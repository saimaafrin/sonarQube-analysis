
import sys
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'

def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    # Add the path to sys.path
    sys.path.append(path_to_append)

    # Update the configuration file
    config = ConfigParser()
    config.read(config_file)
    config['DEFAULT']['path'] = path_to_append
    with open(config_file, 'w') as f:
        config.write(f)

    return config, config_file

# Call the function
config, config_file = task_func()

# Print the output
print(config)
print(config_file)