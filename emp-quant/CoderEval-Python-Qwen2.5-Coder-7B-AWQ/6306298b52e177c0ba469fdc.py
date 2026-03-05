from xml.etree import ElementTree as ET

def xml_children_as_dict(node):
    return {child.tag: child for child in node}