
import csv
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    # Create a CSV file and write the IP addresses
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['IP Address'])
        # Generate and write IP addresses in the specified range
        for ip in IPv4Network(ip_range):
            writer.writerow([str(ip)])

    # Return the path to the generated CSV file
    return csv_path