import os
import json
import logging

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    if overrides is None:
        overrides = {}
    
    config_dict = {}
    error_logs = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config_data = json.load(file)
                
                # Resolve environment variables if required
                if resolve_env:
                    config_data = {k: v.replace('${' + env_var + '}', os.getenv(env_var)) for k, v in config_data.items() if isinstance(v, str)}
                
                # Apply overrides
                config_data.update(overrides.get(filename, {}))
                
                config_dict[filename] = config_data
        except (FileNotFoundError, PermissionError) as e:
            logging.error(f"Failed to read configuration file '{filename}': {e}")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse configuration file '{filename}': {e}")
            error_logs.append(e)
    
    return config_dict, error_logs