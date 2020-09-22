import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("Enter the message")
portno=int(input("Enter the port number"))
s.sendto(str.encode(msg),('127.0.0.1',portno))
data,addr=s.recvfrom(1024)
print(data,addr)
