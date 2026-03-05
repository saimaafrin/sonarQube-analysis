
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
            headers = root.tag.split('}')[-1]  # Extract the tag name as the header
            writer.writerow([headers])
            
            # Write the data rows
            for child in root:
                writer.writerow([child.tag.split('}')[-1], child.text])
        
    except ET.ParseError as e:
        raise ET.ParseError(f"Failed to parse XML content: {e}")
    except IOError as e:
        raise IOError(f"Failed to write to CSV file: {e}")