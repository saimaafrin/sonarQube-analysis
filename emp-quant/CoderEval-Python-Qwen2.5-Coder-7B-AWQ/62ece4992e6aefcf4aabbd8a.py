import os
import json
import logging

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    config_dict = {}
    error_records = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config_data = json.load(file)
                
                if resolve_env:
                    config_data = {k: v.format(**os.environ) if isinstance(v, str) else v for k, v in config_data.items()}
                    
                if overrides:
                    config_data.update(overrides.get(filename, {}))
                
                config_dict[filename] = config_data
        except (FileNotFoundError, PermissionError) as e:
            logging.error(f"Failed to read configuration file '{filename}': {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse configuration file '{filename}': {e}")
            error_records.append(logging.LogRecord('json', logging.ERROR, None, 0, f"Failed to parse configuration file '{filename}'", (), None))
    
    return config_dict, error_records