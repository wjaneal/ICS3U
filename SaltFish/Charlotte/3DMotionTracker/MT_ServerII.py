
# -*- coding: cp1252 -*-
# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen
# this is the server

import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# associate the socket with a port
host = '' # can leave this blank on the server side
port = 50000
s.bind((host, port))

while(1):
    # accept "call" from client
    s.listen(1)
    conn, addr = s.accept()
    print 'client is at', addr
    
    # read string from client (assumed here to be so short that one call to
    # recv() is enough), and make multiple copies (to show the need for the
    # "while" loop on the client side)

    data = conn.recv(1000000)


    # wait for the go-ahead signal from the keyboard (to demonstrate that
    # recv() at the client will block until server sends)
    #z = raw_input()    
    # now send
    print "The server received the following data: ", data
    conn.send(data+" thanks - data received")
conn.close()
    #  close the connection
