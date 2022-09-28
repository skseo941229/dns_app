from flask import Flask, request, Response
from socket import socket, AF_INET, SOCK_DGRAM

app = Flask(__name__)

def calculate_fib(number):
    if number <=1:
        return 1
    elif number ==2:
        return 1
    else:
        return calculate_fib(number-1)+calculate_fib(number-2)

@app.route('/register', methods =["PUT"])
def registration():
    hostname = request.json['hostname']
    ip = request.json['ip']
    as_ip = request.json['as_ip']
    as_port = request.json['as_port']  
    print(hostname, ip, as_ip, as_port)
    MESSAGE = "TYPE=A\nNAME="+hostname+"\n"+"VALUE="+ip+"\nTTL=10"
    sock = socket(AF_INET, SOCK_DGRAM)
    as_port = int(as_port)
    sock.sendto(MESSAGE.encode(), (as_ip, as_port))
    return Response('Registration was successful', status=201)

@app.route('/fibonacci', methods=['GET']) 
def returnfib():
    number = request.args.get('number', type = int) 
    if isinstance(number, int):
        result = calculate_fib(number)
        return Response(str(result), status=200)
    else:
        return Response("Please only put integer", status=400)
    
app.run(host='0.0.0.0',
        port=9090,
        debug=True)