# FIND ADDRESS BLOCK, FIRST ADDRESS AND LAST ADDRESS:

import ipaddress  # IMPORT IPADDRESS
import math       # IMPORT MATH MODULE

# GET THE IP ADDRESS
ip=input("Enter the ip address:")

# IT SPLITS THE IP ADDRESS AND THE MASK
i=ip.split("/")                    
p=i[1]
l=32-int(p)

# FIND THE ADDRESS SPACE WITH THIS FORMULA
val=math.pow(2,int(l))
n=ipaddress.IPv4Network(ip)

# ASSIGN FIRST AND THE LAST ADDRESS
first,last=n[1],n[-1]
print("ADDRESS BLOCK",int(val)) # PRINT THE BLOCK
print("FIRST ADDRESS",first)    # PRINT THE FIRST ADDRESS
print("LAST ADDRESS",last)      # PRINT THE LAST ADDRESS









