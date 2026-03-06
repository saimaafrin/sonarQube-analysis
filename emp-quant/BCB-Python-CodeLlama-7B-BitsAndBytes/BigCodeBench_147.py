
import socket
from ipaddress import IPv4Network
from threading import Thread

def task_func(ip_range, port):
    # Create a dictionary to store the results
    results = {}

    # Iterate over the IP addresses in the range
    for ip in IPv4Network(ip_range):
        # Create a new thread to check the port status
        t = Thread(target=check_port, args=(ip, port))
        t.start()
        # Add the result to the dictionary
        results[ip] = t.result()

    return results

def check_port(ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the IP address and port
    try:
        s.connect((ip, port))
        # If we get here, the port is open
        return True
    except:
        # If we get here, the port is closed
        return False
    finally:
        # Close the socket
        s.close()

    # Call the function and print the results
    results = task_func(ip_range, port)
    print(results)