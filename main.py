import socket 
import sys
import signal

def signal_handler(signum, frame):
    print "Signal handler called with", signum
    sys.exit()
    
host = "localhost" 

if len(sys.argv) == 2:
    port = int(sys.argv[1]) 
else:
    print "Wrong usage format! Correct usage format: main.py <port_number>"
    sys.exit()

backlog = 5 
size = 1024 

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port)) 
except:
    print "Unable to create socket!"
    sys.exit()

s.listen(backlog) 
client, address = s.accept()

while 1:  
    data = client.recv(size) 
    if not data: 
    	client.close()
    	break
    else:
    	client.send(data) 


