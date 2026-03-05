import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Use YAML to read various information in plugin_dir and return the information in dictionary form.
    """
    flatten_dict = {}
    for root, dirs, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    flatten_dict.update(data)
    return flatten_dict