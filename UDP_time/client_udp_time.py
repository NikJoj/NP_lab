import socket
import datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ('127.0.0.1',3006)
n = 0
try:
		msg = str(datetime.datetime.now().time())[0:8]
		print("Sending Time : "+msg)
		sent = sock.sendto(msg,server)
		data,server = sock.recvfrom(20)
		print("Received Time: "+data)
		
finally:
	sock.close()
