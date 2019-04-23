from ftplib import FTP

def uploadFile(filename):
 #filename = 'ns2_wired.png' 
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile(filename):
 #filename = 'ns2_wired.png' 
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

ftp = FTP('')
ftp.connect('localhost',1026)
print 'Connecting to FTP server localhost at port: 1026'
ftp.login('nikhil','12345')
print 'Logging in as user nikhil'
ftp.cwd('/Desktop/NP_lab/ConcurrentFileServer/ServerFiles')

file_name = raw_input("Enter the file to download: ")

filelist = []
ftp.retrlines('LIST',filelist.append)   
f=0
flag=0

for f in filelist:
    if file_name in f:
        flag=1
        downloadFile(file_name)
        print "File Found and Downloaded!"

    
if flag==0:
    print "File not found!"