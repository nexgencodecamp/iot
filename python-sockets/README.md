Peer to peer networking example in Python for communication across the network

What is it?
-----------
An example of a remote keyboard connection from a laptop/wireless keyboard to a Raspberry Pi using sockets

How to run the example
----------------------
Both examples run on python3.

It really helps if you can ssh into your raspberry pi to run this example.
Copy sock-server.py to a raspberrypi
Make sure the IP address in sock-server.py on line 5 is the IP address of the RPi (the server being connected to)

Start sock-server.py:
python3 sock-server.py

On your machine (Mac or Windows), start keyboard.py:
python3 keyboard.py

Using your arrow keys, press a few of them. On the Raspberry Pi you should see the following output:

Received "U"
Received "R"
Received "L"
Received "D"

In the above example you pressed up, right, left and then down arrow keys.
