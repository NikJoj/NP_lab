# Python TCP Client A
import socket 
import time
from ftplib import FTP

def downloadFile(filename):
 #filename = 'ns2_wired.png' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

ftp = FTP('')

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
file_name = raw_input("Enter filename to Download:") 
 
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClient.connect((host, port))
tcpClient.send(file_name)   

time.sleep(1) 



ftp.connect('localhost',1026)
ftp.login('nikhil','12345')
ftp.cwd('/Desktop/NP_lab') #replace with your directory

filelist = [] #to store all files
ftp.retrlines('LIST',filelist.append)    # append to list  
f=0
flag=0

for f in filelist:
    print f

for f in filelist:
    if file_name in f:
        #do something
        flag=1
        print "File Found and Downloaded!"
        downloadFile(file_name)
    


if flag==0:
    print "File not found!"
    #do your processing here


#data = tcpClient.recv(BUFFER_SIZE)
#print " Client2 received data:", data

tcpClient.close() 