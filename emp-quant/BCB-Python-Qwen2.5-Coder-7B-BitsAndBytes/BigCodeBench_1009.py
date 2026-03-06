
import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    try:
        # Parse the XML content
        root = ET.fromstring(xml_content)
        
        # Extract data from XML
        data = []
        for child in root:
            row_data = {}
            for subchild in child:
                row_data[subchild.tag] = subchild.text
            data.append(row_data)
        
        # Write data to CSV
        with open(output_csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    except ET.ParseError as e:
        print(f"ET.ParseError: {e}")
    except IOError as e:
        print(f"IOError: {e}")