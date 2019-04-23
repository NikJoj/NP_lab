import socket 
import random
from threading import Thread 
from SocketServer import ThreadingMixIn 
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        data = conn.recv(2048)
        print "Server received data (filename):", data
        server = FTPServer(("127.0.0.1", 1026), handler)
        #print 'FTP server using port: '
        server.serve_forever()

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
authorizer = DummyAuthorizer()
authorizer.add_user("nikhil", "12345", "/home/nikhil", perm="elradfmw")
#authorizer.add_anonymous("/home/nikhil", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

while True: 
    tcpServer.listen(4) 
    print "Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 