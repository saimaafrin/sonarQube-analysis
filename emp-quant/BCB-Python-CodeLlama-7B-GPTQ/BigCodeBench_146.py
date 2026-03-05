import subprocess
from ipaddress import IPv4Network
def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    The function returns a dictionary with IP addresses as keys and a boolean value indicating their active status (True if the ping is successful, False otherwise).
    The function should raise the exception for: subprocess.CalledProcessError: If a ping command fails due to a subprocess error.
    The function should output with:
        dict: A dictionary mapping IP addresses to their active status.
    """
    # Create a dictionary to store the IP addresses and their active status
    ip_dict = {}

    # Create an IPv4Network object to represent the IP address range
    ip_range = IPv4Network(ip_range)

    # Iterate over the IP addresses in the range
    for ip in ip_range:
        # Create a subprocess to run the ping command
        try:
            # Run the ping command and get the output
            output = subprocess.check_output(["ping", "-c", "1", str(ip)])

            # Check if the ping was successful
            if "64 bytes from" in output:
                # The ping was successful, so the IP address is active
                ip_dict[ip] = True
            else:
                # The ping failed, so the IP address is not active
                ip_dict[ip] = False
        except subprocess.CalledProcessError:
            # The ping command failed, so the IP address is not active
            ip_dict[ip] = False

    # Return the dictionary with the IP addresses and their active status
    return ip_dict
ip_range = "192.168.1.0/24"