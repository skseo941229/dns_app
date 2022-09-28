from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('0.0.0.0', 53533))
file_name = "dns.txt"

while True:
	msg, addr = sock.recvfrom(1024)
	ttmp = msg
	message1 = msg.decode()
	message = message1.split("\n")
	temp_dict = {}
	for msg in message:
		tmp_text = msg.split('=')
		temp_dict[tmp_text[0]] = tmp_text[1]
	if 'VALUE' in temp_dict and 'TTL' in temp_dict:
		str1 = "TYPE="+temp_dict['TYPE']+",NAME="+temp_dict['NAME']+",VALUE="+temp_dict['VALUE'] +",TTL="+temp_dict['TTL']+"\n"
		with open(file_name, 'a') as f:
			f.write(str1)
		
	else:
		file1 = open(file_name, 'r')
		Lines = file1.readlines()
		for line in Lines:
			tmp = line.split(",")
			if tmp[1].split("=")[1] == temp_dict['NAME']:
				MESSAGE = line
				sock.sendto(MESSAGE.encode(), addr)
				#MESSAGE = tmp[2].split("=")[1]
				#sock.sendto(MESSAGE.encode(), addr)
				 		
		
		
				
