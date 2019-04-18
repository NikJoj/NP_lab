import socket, sys
from struct import *

#create a raw socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

while True:
    print s.recvfrom(65565)