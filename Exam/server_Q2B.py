import sys
import socket
from thread import *
import thread

ip = "127.0.0.1"
port = 6000

news=[]
sports=[]
entertainment=[]

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(10)

def client():
	while True:
		conn, addr = s.accept()
		conn.send("Connection attempt has reached server")
		topic = conn.recv(1024)
		print " has subscribed to " + topic
	
		if (topic == "news"):
			news.append(conn)
		elif (topic == "sports"):
			sports.append(conn)
		elif (topic == "entertainment"):
			entertainment.append(conn)
		
		
		


def broadcast():
	while True:
		article = raw_input("Enter article to broadcast with topic as first word ")
		g = article.split()
		topic = g[0]
		article = article.strip(g[0])
		print article
		if (topic == "news"):
			for x in news:
				#print x
				x.send(article)
		elif (topic == "sports"):
			for x in sports:
				x.send(article)
		elif (topic == "entertainment"):
			for x in entertainment:
				x.send(article)

thread.start_new_thread(broadcast,())
client()

s.close()
