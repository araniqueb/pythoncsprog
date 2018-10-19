import socket
import time
import datetime

HOST = '127.0.0.1'
PORT = 56789
Message = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
x = raw_input("Enter x: ")
y = raw_input("Enter y: ")
z = raw_input("Enter z: ")
degree = raw_input("Enter degree: ")
timestamp = datetime.datetime.now()
Message = str(x)+','
Message += str(y)+','
Message += str(z)+','
Message += str(degree)+ ','
Message += str(timestamp)
s.send(Message)
data = s.recv(1024)
print('Received data ', data)
s.close()
