import serial
import time
import re

print("Start")

# MAC
# port = "/dev/cu.HC-05-DevB"
# port = "/dev/tty.HC-05-DevB"

# Windows
# port = "COM4"

# Raspberry Pi
port = "/dev/rfcomm1"

# Start communications with the bluetooth unit
bluetooth = serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput()

while True:
    bytesToRead = bluetooth.inWaiting()
    value = re.sub('[<>]', '', bluetooth.read(bytesToRead).decode())
    print(value)
    time.sleep(1)  # A pause between bursts

bluetooth.close()
print("Done")
