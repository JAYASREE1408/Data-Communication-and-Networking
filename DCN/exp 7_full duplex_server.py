import socket
import sys
import time
x=socket.socket()
host_name=socket.gethostname()
print("Server will start on the Host:",host_name)
port=(int(input("Enter the port number!")))
x.bind((host_name,port))
print("Server has done binding to the Host and the Port successfully!!!")
print("Server is waiting  for incoming connections...")
x.listen(1)
connection,address=x.accept()
print(address,"has connected to the Server and is now online!")
while True:
    display_msg=input(str("Enter the message:"))
    display_mesg=display_msg.encode()
    connection.send(display_mesg)
    print("Message has been sent successfully!!!") 
    in_mesg=connection.recv(1024)
    in_msg=in_mesg.decode()
    print("Client :",in_mesg)
