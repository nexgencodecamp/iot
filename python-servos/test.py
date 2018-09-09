import RPi.GPIO as IO
import time                  # calling for time to provide delays in program
IO.setwarnings(False)        # do not show any warnings
IO.setmode(IO.BCM)

IO.setup(25, IO.OUT)             # initialize GPIO25 as an output
p = IO.PWM(25, 50)              # GPIO25 as PWM output, with 50Hz frequency

p.start(7.5)  # generate PWM signal with 7.5% duty cycle

while 1:         # execute loop forever
    p.ChangeDutyCycle(7.5)  # set servo position to 90º

    time.sleep(1)           # sleep for 1 second

    p.ChangeDutyCycle(12.5)  # set servo position to 180º
    time.sleep(1)           # sleep for 1 second

    p.ChangeDutyCycle(2.5)  # set servo position to 0º
    time.sleep(1)
