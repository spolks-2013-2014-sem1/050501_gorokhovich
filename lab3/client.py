#!/usr/bin/env python2

import socket, os, sys, signal

def signal_handler(signum, frame):
    print "Signal handler called with", signum
    sys.exit()

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

class Client:
    host = ""
    port = 0

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        self.requestFile(client_socket)

    def createDirectory(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def requestFile(self, client_socket):
        print "Enter file name with extension"
        fileName = raw_input()
        client_socket.send(fileName)

        path = "./recievedFiles/" + os.path.basename(fileName)
        self.createDirectory(path)
        fileName = path
        receivedFile = open(fileName, 'w')
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            receivedFile.write(data)
        receivedFile.close()
        print "Data Received successfully"
        exit()

if len(sys.argv) == 3:
    client = Client(sys.argv[1], int(sys.argv[2]))
    client.connect()
else:
    print "Wrong usage format! Correct usage format: client.py <adress> <port_number>"
    sys.exit()
    
    