import xml.etree.ElementTree as ET
import csv
def task_func(xml_content, output_csv_path):
    try:
        # Parse the XML content
        root = ET.fromstring(xml_content)
        
        # Open the CSV file for writing
        with open(output_csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header row
            headers = root[0].attrib.keys()
            writer.writerow(headers)
            
            # Write the data rows
            for item in root:
                row = [item.attrib.get(header, '') for header in headers]
                writer.writerow(row)
    
    except ET.ParseError as e:
        # Handle XML parsing errors
        raise Exception(f"Failed to parse XML: {e}")
    
    except IOError as e:
        # Handle file I/O errors
        raise Exception(f"Failed to write to CSV file: {e}")
xml_content = """
<root>
    <item id="1" name="Item 1" price="10.99"/>
    <item id="2" name="Item 2" price="19.99"/>
</root>
"""
output_csv_path = "output.csv"