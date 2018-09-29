import serial
import time
import re

print("Start")

# MAC
port = "/dev/cu.HC-05-DevB"

# Start communications with the bluetooth unit
bluetooth = serial.Serial(port, 9600)
print("Connected")
bluetooth.flushInput()

while True:
    bytesToRead = bluetooth.inWaiting()
    value = re.sub('[<>]', '', bluetooth.read(bytesToRead).decode())
    print(value)
    time.sleep(1)  # A pause between bursts

bluetooth.close()  # Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
