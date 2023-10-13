# Goal is to allow the user to save strings, and then be able to send them later on

# what is necessary:
# if not peer-to-peer
# the program must peroidically check for information being sent, and then store the mesasge
# application must be always running (if not using other computers)

# if peer-to-peer:
# program must allow other computers to store encrypted data locally on the device
# program must get the computer to send data when requested
import socketserver

class SocketServer:
    # makes the device continuously serve requests
    socketserver.ServerForever(1)




# user needs to do some specific action that lets them no longer take requests
userAction = bool
if socketserver.timeout(5):
    print("Server has Timed out. Restart to continue chatting")
    socketserver.server_close()




