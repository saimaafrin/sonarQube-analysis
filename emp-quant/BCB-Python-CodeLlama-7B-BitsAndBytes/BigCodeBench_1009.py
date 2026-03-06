
import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Create a CSV writer
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Name', 'Age', 'Gender'])

        # Iterate over the XML elements and write the data to the CSV file
        for person in root.findall('.//person'):
            name = person.find('name').text
            age = person.find('age').text
            gender = person.find('gender').text
            writer.writerow([name, age, gender])

    # Close the CSV file
    csvfile.close()