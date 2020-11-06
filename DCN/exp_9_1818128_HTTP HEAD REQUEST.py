# HTTP HEAD REQUEST:

# IMPORT THE SOCKET MODULE
import socket
# HTTP SOCKET S IS CREATED WITH SOME OPERATIONS TO BE PERFORMED
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # USING SOCKET CONNECT TO THE WEBSITE WITH PORT NO 80
    s.connect(("gct.ac.in" , 80))
    # SENDING THE HEAD REQUEST TO GCT.AC.IN
    s.sendall(b"HEAD / HTTP/1.1\r\nHost: gct.ac.in\r\nAccept: text/html\r\n\r\n")
    # PRINT THE INFORMATION OBTAINED FROM THE HTTP SOCKET
    print(str(s.recv(1024), 'utf-8')) 
