import csv
from ipaddress import IPv4Network
def task_func(ip_range, csv_path):
    """
    Generates a CSV file listing all IP addresses in the specified IP range.
    
    Parameters:
    ip_range (str): The IP range in CIDR notation (e.g., '192.168.1.0/24').
    csv_path (str): The path to the generated CSV file.
    
    Returns:
    str: The path to the generated CSV file.
    """
    # Create an IPv4Network object from the given IP range
    network = IPv4Network(ip_range)
    
    # Open the CSV file for writing
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['IP Address'])
        
        # Iterate over all IP addresses in the network and write them to the CSV file
        for ip in network.hosts():
            writer.writerow([str(ip)])
    
    # Return the path to the generated CSV file
    return csv_path