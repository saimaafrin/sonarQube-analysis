import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Use YAML to read various information in plugin_dir and return the information in dictionary form.
    """
    spec_files = [f for f in os.listdir(plugin_dir) if f.endswith('.yaml')]
    flatten_dict = {}
    
    for file in spec_files:
        with open(os.path.join(plugin_dir, file), 'r') as f:
            data = yaml.safe_load(f)
            flatten_dict.update(data)
    
    return flatten_dict