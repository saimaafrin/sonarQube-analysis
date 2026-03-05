
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
        raise Exception(f"Failed to parse XML content: {e}")
    
    except IOError as e:
        # Handle CSV file writing errors
        raise Exception(f"Failed to write to CSV file: {e}")