import csv
from ipaddress import IPv4Network
def task_func(ip_range, csv_path):
    # Create an IPv4Network object from the given IP range
    network = IPv4Network(ip_range)
    
    # Open the CSV file for writing
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write each IP address in the network to a new row in the CSV file
        for ip in network.hosts():
            writer.writerow([str(ip)])
    
    # Return the path to the generated CSV file
    return csv_path