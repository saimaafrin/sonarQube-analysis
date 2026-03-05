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
            headers = root.tag.split('.')
            writer.writerow(headers)
            
            # Write the data rows
            for child in root:
                row = [child.tag.split('.')[-1], child.text]
                writer.writerow(row)
    except ET.ParseError as e:
        # Handle XML parsing errors
        raise e
    except IOError as e:
        # Handle file I/O errors
        raise e
xml_content = """
<root>
    <item>
        <name>Item 1</name>
        <value>Value 1</value>
    </item>
    <item>
        <name>Item 2</name>
        <value>Value 2</value>
    </item>
</root>
"""
output_csv_path = 'output.csv'