import yaml

def _dump_string(obj, dumper=None):
    """
    Given a python object and serialize it into a YAML stream

    Args:
        obj: python object

    Returns:
        YAML stream
    """
    if dumper is None:
        return yaml.dump(obj)
    else:
        return yaml.dump(obj, Dumper=dumper)