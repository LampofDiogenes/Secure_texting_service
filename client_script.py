# Goal is to allow the user to save strings, and then be able to send them later on

# what is necessary:
    # if not peer-to-peer
    # the program must peroidically check for information being sent, and then store the mesasge
    # application must be always running (if not using other computers)

    # if peer-to-peer:
    # program must allow other computers to store encrypted data locally on the device
    # program must get the computer to send data when requested

    # program must force users to create a unique usnername, or else assign it to the user

import socketserver
import socket

# creating a socket that will allow computers to listen and then connect
# this will allow computers to communicate to each other
# AF_INET is just something that I need, and SOCK_stream is TCP protocol
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

random_address = "https://pubchem.ncbi.nlm.nih.gov/compound/Histamine"

try:
    # finding an IP to host a connection
    host_ip = socket.gethostbyname(random_address)
except:
    # telling developer what went wrong
    print("listening failed")

try: 
    # connecting to found IP address
    client_socket.connect(host_ip, port)
    print('successfully connected')
except:
    print('not able to connect')

try:
    client_socket.close()
    print("successfully left server")
except:
    print('Error leaving server')

