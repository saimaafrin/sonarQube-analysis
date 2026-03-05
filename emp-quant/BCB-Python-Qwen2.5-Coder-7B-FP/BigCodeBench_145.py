import csv
from ipaddress import IPv4Network
def task_func(ip_range, csv_path):
    # Create an IPv4Network object from the given IP range
    network = IPv4Network(ip_range)
    
    # Open the CSV file in write mode
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['IP Address'])
        
        # Iterate over all IP addresses in the network
        for ip in network.hosts():
            # Write each IP address as a row in the CSV file
            writer.writerow([str(ip)])
    
    # Return the path to the generated CSV file
    return csv_path