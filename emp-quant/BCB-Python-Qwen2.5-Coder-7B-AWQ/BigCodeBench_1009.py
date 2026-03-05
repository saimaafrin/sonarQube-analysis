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
            headers = root.tag
            writer.writerow(headers)
            
            # Write the data rows
            for child in root:
                row = [child.tag, child.text]
                writer.writerow(row)
    except ET.ParseError as e:
        # Handle XML parsing errors
        raise Exception(f"Failed to parse XML content: {e}")
    except IOError as e:
        # Handle CSV file writing errors
        raise Exception(f"Failed to write to CSV file: {e}")
xml_content = """
<root>
    <child1>Value1</child1>
    <child2>Value2</child2>
</root>
"""
output_csv_path = "output.csv"