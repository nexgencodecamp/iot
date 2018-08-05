import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.4', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(32)
            if data:
                print('Received "%s"' % data.decode("utf-8"))
                # connection.sendall(data)
            else:
                print('No more data from', client_address)
                break
    finally:
        connection.shutdown(1)
        connection.close()