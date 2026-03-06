
import csv
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    # Create a list to store the IP addresses
    ip_list = []

    # Create a network object from the IP range
    network = IPv4Network(ip_range)

    # Iterate over the hosts in the network and add their IP addresses to the list
    for host in network.hosts():
        ip_list.append(str(host))

    # Open the CSV file and write the IP addresses to it
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ip in ip_list:
            writer.writerow([ip])

    # Return the path to the generated CSV file
    return csv_path