import csv
from ipaddress import IPv4Network
def task_func(ip_range, csv_path):
    """
    Generates a CSV file listing all IP addresses in the specified IP range.
    Each IP address is written as a row in the CSV file.
    """
    # Create a list of all IP addresses in the specified IP range
    ip_list = []
    for ip in IPv4Network(ip_range):
        ip_list.append(ip)

    # Write the list of IP addresses to a CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['IP Address'])
        for ip in ip_list:
            writer.writerow([ip])

    return csv_path
ip_range = '192.168.0.0/24'
csv_path = 'ip_list.csv'