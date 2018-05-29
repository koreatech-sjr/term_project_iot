from bluetooth import *

# Create the client socket
client_socket = BluetoothSocket(RFCOMM)

client_socket.connect(("b8:27:eb:6b:4e:9a", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()
