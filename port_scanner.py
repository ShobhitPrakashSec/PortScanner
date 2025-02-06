import socket # import the socket module

# Ger user input and taret Hostname or IP address
target = input("Enter the IP address or Hostname to scan: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

# scan each port in given range
def scan_port(ip, port):
    try:
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set the timeout for connection attempt
        s.settimeout(1)
        # connect to the target, this will return 0 if the port is open
        s.connect((ip, port)) 
        print(f"Port {port} is open") # print the port number
        # close the connection
        s.close() 
    except Exception as e:
        print(f"Error scanning Port {port}: {e}, Port is closed") # print the port number
    
# loop through the port range and call the scan_port function
for port in range(start_port, end_port+1):
    scan_port(target, port) # call the scan_port function
