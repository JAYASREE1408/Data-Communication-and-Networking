import socket
import sys
import time
x=socket.socket()
host_name=input(str("Enter the hostname of the Server!!!"))
port=(int(input("Enter the port number!")))
x.connect((host_name,port))
print("Hey!You can have a chat now.You are connected to chat Server...")
while True:
    incoming_mesg=x.recv(1024)
    incoming_msg=incoming_mesg.decode()
    print("Server :",incoming_msg)
    msg=input(str("Enter the message:"))
    Msg=msg.encode()
    x.send(Msg)
    print("Message has been sent successfully!!!")
