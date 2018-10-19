import socket


HOST = '127.0.0.1'
PORT = 56789

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connection address: ', addr)
Message = ''
while 1:
    data = conn.recv(1024)
    if not data:
        break
    print('Received data: ', data)
    List = data.split(',')
    x = float(List[0]) / 2.0
    y = float(List[1]) / 2.0
    z = float(List[2]) / 2.0
    degree = float(List[3]) / 2.0
    Message = str(x) + ', '
    Message += str(y) + ', '
    Message += str(z) + ', '
    Message += str(degree)
    conn.send(Message)
conn.close()
s.close()
