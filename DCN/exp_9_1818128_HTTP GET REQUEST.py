# HTTP GET REQUEST:

# IMPORT THE SOCKET MODULE
import socket
# HTTP SOCKET S IS CREATED WITH SOME OPERATIONS TO BE PERFORMED
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # USING SOCKET CONNECT TO THE WEBSITE WITH PORT NO 80
    s.connect(("gct.ac.in" , 80))
    # READS THE HOME PAGE OF THE WEBSITE USING GET REQUEST
    s.sendall(b"GET / HTTP/1.1\r\nHost: gct.ac.in\r\nAccept: text/html\r\nConnection: close\r\n\r\n") 
    
    while True: # WHILE LOOP PROCESS THE RECEIVED DATA

        # IF THERE IS NO ERROR THEN RECV RETURNS THE BYTES RECEIVED
        data = s.recv(1024) 
        
        if not data: # IF NO DATA RECEIVED THEN BREAK THE LOOP
            break

        # DECODE AND PRINT THE DATA RECEIVED    
        print(data.decode()) 
