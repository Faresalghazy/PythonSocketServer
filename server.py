# Program to communicate with mobile app over sockets by Fares Al Ghazy
import socket
import sys

# Global variables
PORT = int(0)  # Port to communicate over, 0 will find any free port

HOST = '0.0.0.0'  # recieve from any ip

# -----------------Main-------------------------#
# Check if user has specified port
if len(sys.argv) == 2:
    port = int(sys.argv[1])

serversocket = socket.socket()
serversocket.bind((HOST, PORT))

# Specify to only listen to one device
serversocket.listen(1)
print("Socket now listening at port " + str(serversocket.getsockname()[1]))
# Get and display input

while True:
    # Find client socket

    connection, address = serversocket.accept()

    receivedstring = connection.recv(10).decode('utf-8')[2:]

    print(receivedstring)

print("End of program")

