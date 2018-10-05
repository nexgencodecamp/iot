#!/usr/bin/env python3

"""
File: gpiozero-test.py

This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.

Documentation: https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice

"""

__author__ = "Pete Januarius"
__version__ = "0.1.0"
__license__ = "MIT"

import curses
import serial
import time
import re
import sys
import termios
import tty
import os
from gpiozero import PWMOutputDevice
from time import sleep

# ///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26  # IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19  # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

button_delay = 0.2

# Raspberry Pi
port = "/dev/rfcomm1"

MANUAL = 1
AUTONOMOUS = 2

# Handles keyboard input


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def allStop():
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0


def forwardDrive():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0


def reverseDrive():
    forwardLeft.value = 0
    reverseLeft.value = 0.8
    forwardRight.value = 0
    reverseRight.value = 0.8


def spinLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.8
    forwardRight.value = 0.8
    reverseRight.value = 0


def spinRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0.8


def forwardTurnLeft():
    forwardLeft.value = 0.2
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0


def forwardTurnRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.2
    reverseRight.value = 0


def reverseTurnLeft():
    forwardLeft.value = 0
    reverseLeft.value = 0.2
    forwardRight.value = 0
    reverseRight.value = 0.8


def reverseTurnRight():
    forwardLeft.value = 0
    reverseLeft.value = 0.8
    forwardRight.value = 0
    reverseRight.value = 0.2


def main(stdscr):
    print("Start")

    # Start communications with the bluetooth unit
    #bluetooth = serial.Serial(port, 9600)
    # print("Connected")
    # bluetooth.flushInput()

    quit = False
    mode = MANUAL

    while True:
        if(quit == True):
            break
        elif(mode == MANUAL):
            print("Switching to manual mode...")

            while True:
                char = getch()

                # TODO - add a lastchar variable and check if char != lastchar

                if (char == "q"):
                    quit = True
                    break

                if (char == "p"):
                    print("Stop!")
                    allStop()

                if (char == "a"):
                    print("Left pressed")
                    time.sleep(button_delay)
                    forwardTurnLeft()

                elif (char == "d"):
                    print("Right pressed")
                    time.sleep(button_delay)
                    forwardTurnRight()

                elif (char == "w"):
                    print("Up pressed")
                    time.sleep(button_delay)
                    forwardDrive()

                elif (char == "s"):
                    print("Down pressed")
                    time.sleep(button_delay)
                    reverseDrive()

                elif (char == "k"):
                    print("k pressed")
                    time.sleep(button_delay)
                    reverseTurnLeft()

                elif (char == "l"):
                    print("l pressed")
                    time.sleep(button_delay)
                    reverseTurnRight()

                elif (char == "h"):
                    print("h pressed")
                    time.sleep(button_delay)
                    spinLeft()

                elif (char == "j"):
                    print("j pressed")
                    time.sleep(button_delay)
                    spinRight()
                elif (char == "2"):
                    print("2 pressed")
                    time.sleep(button_delay)
                    mode = AUTONOMOUS
                    break
                sleep(0.25)
        elif(mode == AUTONOMOUS):

            # Read incoming bluetooth bytes
            # bytesToRead = bluetooth.inWaiting()
            # value = re.sub('[<>]', '', bluetooth.read(bytesToRead).decode())
            # print(value)

            while(True):
                print("Switching to autonomous mode...")
                # NOTE: stdscr.getchh() will get ASCII values so
                # a = 97, q = 113, 1 = 49
                c = stdscr.getch()
                print(c)

                if (c == 122):
                    # print numeric value
                    stdscr.addstr(str(c) + ' ')
                    stdscr.refresh()
                    # return curser to start position
                    stdscr.move(0, 0)
                elif(c == 113):
                    quit = True
                    break
                elif(c == 49):
                    mode = MANUAL
                    break

                print("sleeping")
                sleep(0.25)

    # bluetooth.close()
    print("Done")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    curses.wrapper(main)
