
import urllib.request
from lxml import etree
import pandas as pd

def task_func(url):
    try:
        # Fetch the XML file from the URL
        with urllib.request.urlopen(url) as response:
            xml_content = response.read()
        
        # Parse the XML content
        xml_tree = etree.fromstring(xml_content)
        
        # Check if the XML structure is valid
        if xml_tree.tag != 'items':
            raise ValueError("XML structure does not match expected format.")
        
        # Extract data from the XML
        items = []
        for item in xml_tree:
            item_data = {}
            for child in item:
                item_data[child.tag] = child.text
            items.append(item_data)
        
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(items)
        
        return df
    except Exception as e:
        raise ValueError(f"Error processing XML: {e}")