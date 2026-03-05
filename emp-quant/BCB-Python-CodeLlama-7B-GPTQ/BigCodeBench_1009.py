import xml.etree.ElementTree as ET
import csv
def task_func(xml_content, output_csv_path):
    """
    Parses XML content from a string and converts it into a CSV format.
    """
    # Parse the XML content
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse XML content: {e}")

    # Create a CSV writer
    with open(output_csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Name", "Age", "Gender"])

        # Write the data rows
        for child in root:
            writer.writerow([child.find("Name").text, child.find("Age").text, child.find("Gender").text])

    return None
xml_content = """
<root>
    <person>
        <Name>John</Name>
        <Age>25</Age>
        <Gender>Male</Gender>
    </person>
    <person>
        <Name>Jane</Name>
        <Age>30</Age>
        <Gender>Female</Gender>
    </person>
</root>
"""
output_csv_path = "output.csv"