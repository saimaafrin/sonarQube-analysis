
import csv
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    # Create an IPv4Network object from the given IP range
    ip_network = IPv4Network(ip_range)

    # Open the CSV file for writing
    with open(csv_path, 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(['IP Address'])

        # Iterate over the IP addresses in the network
        for ip_address in ip_network.hosts():
            # Write the IP address to the CSV file
            csv_writer.writerow([str(ip_address)])

    # Return the path to the generated CSV file
    return csv_path