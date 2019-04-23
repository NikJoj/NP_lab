import socket, sys
from struct import *

print "Menu: "
print "1. Sniff for TCP Packets"
print "2. Sniff for UDP Packets"
choice = input("Enter your option: ")

if (choice == 1):
	#do TCP sniffing
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
	except socket.error , msg:
		print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
	


elif (choice == 2):
	#do UDP sniffing
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
	except socket.error , msg:
		print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
	

while True:
	packet = s.recvfrom(65565)

	packet = packet[0]
	
	#take first 20 characters for the ip header
	ip_header = packet[0:20]
	
	#unpacking
	iph = unpack('!BBHHHBBH4s4s' , ip_header)
	
	version_ihl = iph[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF
	
	iph_length = ihl * 4
	
	ttl = iph[5]
	protocol = iph[6]
	s_addr = socket.inet_ntoa(iph[8]);
	d_addr = socket.inet_ntoa(iph[9]);
	
	if (choice == 2):
		print "---------------------------UDP---------------------------------"
		print 'IP Header Length : ' + str(ihl)
		print 'Protocol : ' + str(protocol) 
		print 'Source Address : ' + str(s_addr) 
		print 'Destination Address : ' + str(d_addr)
		
		udp_header = packet[iph_length:iph_length+20]
		
		udph = unpack('!HHLLBBHHH' , udp_header)
		
		source_port = udph[0]
		dest_port = udph[1]
		sequence = udph[2]
		acknowledgement = udph[3]
		doff_reserved = udph[4]
		udph_length = doff_reserved >> 4
		
		print 'Source Port : ' + str(source_port) 
		print 'Destination Port : ' + str(dest_port)  
		print 'Sequence Number : ' + str(sequence)  
		print 'UDP header length : ' + str(udph_length)
		
		h_size = iph_length + udph_length * 4
		data_size = len(packet) - h_size
		
		#get data from the packet
		data = packet[h_size:]
		
		print 'Data : ' + data
		

	if (choice == 1):
		print "---------------------------TCP---------------------------------"
		print 'Version : ' + str(version) 
		print 'IP Header Length : ' + str(ihl)
		print 'TTL : ' + str(ttl) 
		print 'Protocol : ' + str(protocol) 
		print 'Source Address : ' + str(s_addr) 
		print 'Destination Address : ' + str(d_addr)
		
		tcp_header = packet[iph_length:iph_length+20]
		
		tcph = unpack('!HHLLBBHHH' , tcp_header)
		
		source_port = tcph[0]
		dest_port = tcph[1]
		sequence = tcph[2]
		acknowledgement = tcph[3]
		doff_reserved = tcph[4]
		tcph_length = doff_reserved >> 4
		
		print 'Source Port : ' + str(source_port) 
		print 'Destination Port : ' + str(dest_port)  
		print 'Sequence Number : ' + str(sequence)  
		print 'Acknowledgement : ' + str(acknowledgement)  
		print 'TCP header length : ' + str(tcph_length)
		
		h_size = iph_length + tcph_length * 4
		data_size = len(packet) - h_size
		
		#get data from the packet
		data = packet[h_size:]
		
		print 'Data : ' + data
