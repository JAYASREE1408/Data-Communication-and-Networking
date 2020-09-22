
import socket
UDP_IP_ADDRESS ="192.168.43.93"
UDP_PORT_NO = 6789
Message = ("Hello,  Server!")
bytesToSend = str.encode(Message)
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend, (UDP_IP_ADDRESS, UDP_PORT_NO))

