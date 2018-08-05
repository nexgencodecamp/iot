import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.4', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    message = 'test message9999'
    print('sending "%s"' % message)
    sock.sendall(message)
    # amount_received = 0
    # amount_expected = len(message)
    # while amount_received < amount_expected:
    #     data = sock.recv(32)
    #     amount_received += len(data)
    #     print('received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.shutdown(1)
    sock.close()
