#!/usr/bin/env python2

import socket, os, sys, signal

def signal_handler(signum, frame):
    print "Signal handler called with", signum
    sys.exit()

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

class Server:
   host = ""
   port = 0

   def __init__(self, host, port):
      self.host = host
      self.port = port

   def connect(self):
      try:
         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse socket
         server_socket.bind((self.host, self.port))
      except:
         print "Unable to create socket!"
         sys.exit()
      self.waitForSendFile(server_socket)   

   def waitForSendFile(self, server_socket):
      server_socket.listen(5)
      client_socket, address = server_socket.accept()
      print "Connected to - ",address,"\n"
      while (1):
         data = client_socket.recv(1024)
         print "The following data was received - ",data
         print "Opening file - ",data
         sendingFile = open(data,'r')
         while True:
            sendFileData = sendingFile.read()
            if not sendFileData:
               break
            client_socket.sendall(sendFileData)
            sendingFile.close()
            print "Data sent successfully"
            exit()

if len(sys.argv) == 3:
    server = Server(sys.argv[1], int(sys.argv[2]))
    server.connect()
else:
    print "Wrong usage format! Correct usage format: server.py <adress> <port_number>"
    sys.exit()