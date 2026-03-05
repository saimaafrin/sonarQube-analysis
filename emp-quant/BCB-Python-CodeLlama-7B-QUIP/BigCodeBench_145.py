
import csv
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for ip in IPv4Network(ip_range).hosts():
            csvwriter.writerow([ip])
    return csv_path