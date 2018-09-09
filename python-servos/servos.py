#!/usr/bin/env python3

import sys
import termios
import tty
import os
import RPi.GPIO as IO
import time                  # calling for time to provide delays in program

IO.setwarnings(False)        # do not show any warnings
IO.setmode(IO.BCM)

IO.setup(25, IO.OUT)             # initialize GPIO25 as an output
IO.setup(24, IO.OUT)
p = IO.PWM(25, 50)              # GPIO25 as PWM output, with 50Hz frequency
q = IO.PWM(24, 50)

p.start(7.5)  # generate PWM signal with 7.5% duty cycle
q.start(7.5)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def sweepUp():
    x = 0.1
    while x > 0:
        q.ChangeDutyCycle(2.5 + x)
        x = x + 0.1
        if(x >= 12.5):
            break

        time.sleep(0.05)


def sweepLeft():
    x = 0.1
    while x > 0:
        p.ChangeDutyCycle(2.5 + x)
        x = x + 0.1
        if(x >= 12.5):
            p.ChangeDutyCycle(0)
            break

        time.sleep(0.05)


def sweepRight():
    x = 0.1
    while x > 0:
        p.ChangeDutyCycle(7.5 - x)
        x = x - 0.1
        print(x)
        if(x <= 2.5):
            break

        time.sleep(0.05)


def moveTo():
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)


while True:
    char = getch()

    # TODO - add a lastchar variable and check if char != lastchar

    if (char == "1"):
        print("Sweep Left")
        sweepLeft()

    if (char == "2"):
        print("Sweep Right")
        sweepRight()

    if (char == "3"):
        print("Set Centre")
        p.ChangeDutyCycle(7.5)

    if (char == "4"):
        print("Sweep Up")
        sweepUp()

    if (char == "5"):
        print("MoveTo")
        moveTo()

    if (char == "q"):
        break
