import sys
import socket
from thread import *
import thread

ip = "127.0.0.1"
port = 6000

#tlist=[]


def listening(sock):
	print sock
	while True:
		data = sock.recv(1024)
		print  data

				
#topic = sys.argv[1]
#tlist.append(topic)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))

topic = raw_input("Enter topics[at most 3]: ")
g = topic.split()



print s.recv(1024)
s.send(g[0])

print s.recv(1024)
s.send(g[1])

print s.recv(1024)
s.send(g[2])

print s.recv(1024)


#thread.start_new_thread(listening,(s,0))

while True:
		data = s.recv(1024)
		print  data
#s.close()
