
import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Create a CSV writer
    with open(output_csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

    # Write the CSV header
    csvwriter.writerow(['name', 'age'])

    # Iterate over the XML elements and write the CSV data
    for child in root:
        if child.tag == 'person':
            name = child.attrib['name']
            age = child.attrib['age']
            csvwriter.writerow([name, age])

    # Close the CSV file
    csvfile.close()