
import xml.etree.ElementTree as ET
import csv

def task_func(xml_content, output_csv_path):
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML content: {e}")

    with open(output_csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for child in root:
            writer.writerow([child.tag, child.text])

    return None