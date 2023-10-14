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


class SocketServer:
    # code below makes the device continuously serve requests (but I don't know if I need it)
    # socketserver.ServerForever(1)
    def handle():
        ''

# called every time that a user wants to do something
class BaseRequestHandler(SocketServer):
    # for some reason I need this.
    ''
    # and for some reason I need to override this method here
    def handle():
        ''

# user needs to do some specific action that lets them no longer take requests
userAction = bool
if socketserver.timeout(5):
    print("Server has Timed out. Restart to continue chatting")
    socketserver.server_close()




