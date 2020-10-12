from ARP_1818128 import MACaddress

ip = input("Enter the IP address to find the corresponding MAC address:")

Mac = MACaddress(ip)

if(Mac==0):
    print("There is no MAC address found for the given IP address!")
else:
    print("The corresponding MAC address for the given ip address '"+ip+"' is",Mac)

















