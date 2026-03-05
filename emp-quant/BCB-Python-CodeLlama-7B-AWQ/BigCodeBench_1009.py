import xml.etree.ElementTree as ET
import csv
def task_func(xml_content, output_csv_path):
    """
    Parses XML content from a string and converts it into a CSV format.
    Ensure that the XML content passed to the function is well-formed.
    The output CSV path should be a valid file path where the user has write permissions,
    to prevent IOError.
    The function should raise the exception for:
        ET.ParseError: This exception is raised if the input XML content is malformed or cannot be successfully parsed.
        The exception message includes details about the parsing error.
        IOError: Raised if there is an issue with writing to the specified CSV file path.
        This can happen due to reasons like invalid file path, full disk space, lack of write permissions, etc.
        The exception message provides details about the IO error.
    The function should output with:
        None: The function does not return any value. Instead, it writes the output to
        a CSV file at the specified path.
    """
    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        raise ValueError(f"XML parsing error: {e}")

    with open(output_csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for child in root:
            writer.writerow([child.tag, child.text])