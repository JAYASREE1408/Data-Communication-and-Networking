# HALF DUPLEX COMMUNICATION USING TCP - CLIENT SIDE:

import socket # Import socket module in python
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Create a TCP socket 
    print("Socket created Successfully!!") # If it is created,print this line
except socket.error.msg: 
    print("Error: Failed to create the socket!!") # If it is not created,print this line
portno=int(input("Enter the Port Number:")) # Get port from the client 
s.connect(('127.0.0.1',portno)) # IP address and port no is specified for the connection

while True:
    message=input("Enter the Message:") # Get message from the client
    s.send(str.encode(message)) # Sending message to the server
    data=s.recv(2048) # Receiving the packets sent by the server
    print(data)  # Message received is printed
    if "bye" in str(data):  # To terminate the communication ,enter 'bye'
         break
    elif "continue" in str(data):   # To continue the communication ,enter 'continue'
         continue
