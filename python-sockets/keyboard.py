import socket
import sys
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Socket setup
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.8', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:    
            message = b'U'            
            sock.sendall(message)
        elif char == curses.KEY_DOWN:
            message = b'D'
            sock.sendall(message)
        elif char == curses.KEY_RIGHT:
            message = b'R'
            sock.sendall(message)
        elif char == curses.KEY_LEFT:
            message = b'L'
            sock.sendall(message)
        elif char == 10:
            sock.sendall('STOP')

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

    print(sys.stderr, 'closing socket')
    sock.shutdown(1)
    sock.close()
