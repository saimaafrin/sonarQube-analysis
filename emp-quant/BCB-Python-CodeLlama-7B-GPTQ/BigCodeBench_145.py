import csv
from ipaddress import IPv4Network
def task_func(ip_range, csv_path):
    """
    Generates a CSV file listing all IP addresses in the specified IP range.
    Each IP address is written as a row in the CSV file.

    Args:
        ip_range (str): The IP range to generate the CSV file for.
        csv_path (str): The path to the generated CSV file.

    Returns:
        str: The path to the generated CSV file.
    """
    # Create an IPv4Network object from the IP range
    ip_network = IPv4Network(ip_range)

    # Open the CSV file for writing
    with open(csv_path, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['IP Address'])

        # Iterate over the IP addresses in the IP network
        for ip_address in ip_network.hosts():
            # Write the IP address as a row in the CSV file
            csv_writer.writerow([ip_address])

    # Return the path to the generated CSV file
    return csv_path
ip_range = '192.168.1.0/24'
csv_path = 'ip_addresses.csv'