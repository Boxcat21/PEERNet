import socket

# Get local machine name
host_name = socket.gethostname()

# Get the IP address of the local machine
ip_address = socket.gethostbyname(host_name)

print(f"Local IP address of {host_name}: {ip_address}")
