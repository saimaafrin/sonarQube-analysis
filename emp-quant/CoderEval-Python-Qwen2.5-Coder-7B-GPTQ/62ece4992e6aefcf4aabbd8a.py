import os
import json
import logging

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    config_dict = {}
    error_logs = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                
                if resolve_env:
                    config = {k: v.format(**os.environ) if isinstance(v, str) else v for k, v in config.items()}
                    
                if overrides:
                    config.update(overrides)
                    
                config_dict[filename] = config
        except (FileNotFoundError, PermissionError) as e:
            error_logs.append(logging.LogRecord('load_configurations', logging.ERROR, filename, 0, str(e), (), None))
        except json.JSONDecodeError as e:
            error_logs.append(logging.LogRecord('load_configurations', logging.ERROR, filename, 0, f"Invalid JSON format: {e}", (), None))
    
    return config_dict, error_logs