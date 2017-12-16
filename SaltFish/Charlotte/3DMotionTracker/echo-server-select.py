#!/usr/bin/env python

"""
An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys

host = ''
port = 50000
backlog = 5
size = 10240

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
#sys.stdin was removed from the following input list
#because it is on by default, apparently, in windows.
input = [server]
running = 1
print "Server working"
count = 0    
while running:
    #This line was adjusted according to some guidance on the Internet
    #Regarding socket programming in windows.
    inputready,outputready,exceptready = select.select(input,[],[],1000)
    
    for s in inputready:
        print count, " loops"
        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)
            print "Server received connection"

        elif s == sys.stdin:
            # handle standard input
            print "Received junk"
            junk = sys.stdin.readline()
            running = 0

        else:
            # handle all other sockets
            print "Received something....processing"
            data1 = s.recv(size)
            #data2 = s.recv(size)   
            print data1, " server received this data"
            s.send("Hello - sending data: "+data1)
            #The following lines were commented out to get the server working
            #s.close()
            #input.remove(s)
        count +=1
server.close()

