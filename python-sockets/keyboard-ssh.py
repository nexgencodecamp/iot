import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

m1_forward = GPIO.PWM(11, 100)
m1_forward.start(0)
#m1_reverse = GPIO.PWM(7, 100)
#m1_reverse.start(0)
m2_forward = GPIO.PWM(15, 100)
m2_forward.start(0)
#m2_reverse = GPIO.PWM(13, 100)
#m2_reverse.start(0)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char ==  curses.KEY_ENTER:
                m1_forward.ChangeDutyCycle(50)
                m2_forward.ChangeDutyCycle(50)
                sleep(5)
            elif char == curses.KEY_UP:
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, True)
                print('up')
            elif char == curses.KEY_DOWN:
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
                print('down')
            elif char == curses.KEY_RIGHT:
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)
                print('right')
            elif char == curses.KEY_LEFT:
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, True)
                GPIO.output(15, False)
                print('left')
            elif char == 10:
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()

