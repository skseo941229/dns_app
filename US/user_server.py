from flask import Flask, request, Response
from socket import socket, AF_INET, SOCK_DGRAM
import requests
app = Flask(__name__)

@app.route('/fibonacci')
def fib():
	hostname = request.args.get('hostname')
	fs_port = request.args.get('fs_port')
	number = request.args.get('number')
	as_ip = request.args.get('as_ip')
	as_port = request.args.get('as_port') 

	if not hostname or not fs_port or not number or not as_ip or not as_port:
		return Response("Check parameters", status = 400)
	else:
		sock = socket(AF_INET, SOCK_DGRAM)
		MESSAGE = "TYPE=A\nNAME="+hostname
		as_port = int(as_port)
		sock.sendto(MESSAGE.encode(), (as_ip, as_port))
		msg, addr = sock.recvfrom(1024)
		msg = msg.decode()
		msg = msg.split(",")
		tmp = msg[2].split("=")[1] 
		r = requests.get("http://"+tmp+":"+fs_port+"/fibonacci?number="+number)
		return Response(r, status = 200)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
