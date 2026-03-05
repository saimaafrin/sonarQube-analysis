
import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    try:
        # Parse the XML content
        root = ET.fromstring(xml_content)
        
        # Open the output CSV file for writing
        with open(output_csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write the header row
            writer.writerow(root[0].attrib.keys())
            
            # Write the data rows
            for item in root:
                writer.writerow(item.attrib.values())
        
        return None
    except ET.ParseError as e:
        raise Exception(f"XML parsing error: {e}")
    except IOError as e:
        raise Exception(f"IO error: {e}")