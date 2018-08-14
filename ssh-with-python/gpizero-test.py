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

import sys
import termios
import tty
import os
import time
from gpiozero import PWMOutputDevice
from time import sleep

#///////////////// Define Motor Driver GPIO Pins /////////////////
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
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 1.0
	reverseRight.value = 0


def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 0
	reverseRight.value = 1.0


def spinLeft():
	forwardLeft.value = 0
	reverseLeft.value = 1.0
	forwardRight.value = 1.0
	reverseRight.value = 0


def SpinRight():
	forwardLeft.value = 1.0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 1.0


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


def main():    
    while True:
        char = getch()

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

        elif (char == "1"):
            print("Number 1 pressed")
            time.sleep(button_delay)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
