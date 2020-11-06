# HALF DUPLEX COMMUNICATION USING TCP - SERVER SIDE:
import socket  # Import socket module in python
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Create TCP socket
    print("Socket is created Successfully!") # If it is created,print this line
except socket.error.msg:
    print("Error: Failed to create the socket") # If it is not created,print this line
portno=int(input("Enter the Port Number:")) # Get port no. from the server
s.bind(('127.0.0.1',portno))  # Bind the host ip address and the port number
# Listening to the client's message
s.listen(1)    # Set the client and client'address by the client's request
client,addr = s.accept()   # Accepting the input from the client
while True:
    data=client.recv(2048) # Receiving the packets sent by the client
    print(data)  # Message received is printed
    input1=input("Enter the Message") # Get the message from the server
    client.send(str.encode(input1)) # Send the message to the client
    if "bye" in str(input1): # To terminate the communication ,enter 'bye'
        break
    elif "continue" in str(input1): # To continue the communication ,enter 'continue'
        continue
client.close()
