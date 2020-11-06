# RETRIEVING DATA FROM THE URL :

import urllib.request,urllib.error,urllib.parse      # Importing the URL library
try:
        url=input("Enter the URL")                   # Getting URL from the user
        response=urllib.request.urlopen(url)         # Requesting the data from the URL
        print("The given URL exists!")               # Prints if the entered URL exists
        webContent=response.read()                   # Decoding the URL and response fom the web is read
        print(webContent[0:2000])                    # Prints the web contents
        print("---LIBRARY WEBSITE OF GOVERNMENT COLLEGE OF TECHNOLOGY---") # Prints information about the URL 
        print("* This website gives the information about library facilities at GCT.")
        print("* The library boasts excellent facilities and it serves as a place for quiet reading, group collaboration, individual    research and recreational reading.")
        print("* It provides some information about modern central library.")
        print("* It is associated with more than one lakh documents consisting of technical books, reports, standards and back volumes of journals.")
        print("* It also contains 15,000 books in textbook bank.")
        print("* This website provides some details about issue section, journals, teqip fund and digital library.")
        print("* It also provides some details about the supporting staffs.")
        
except:
        print("The given URL doesn't exists!")       # Prints if the entered URL doesn't exists
