import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
portno=int(input("Enter the port number"))
s.bind(('127.0.0.1',portno))
print("server is waiting")
data,addr=s.recvfrom(1024)
print(data,addr)
s.sendto(data,addr)
