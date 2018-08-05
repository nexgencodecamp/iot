# iot
Code examples and tutorials for the Nexgen IoT/Robotics Event in October

##nodejs-sockets
This example enables you to communicate between 2 computers over Wifi. In the case of the tank,
you may decide to communicate from a laptop to a raspberrypi in the tank. To run the example:

- Install nodejs on your raspberrypi
- Download the source code for this example, the code in the folder 'nodejs-sockets'
- Do an 'npm install' to install all the nodejs modules

To start the code on the raspberry pi:
npm start

You should see a message that says:

listening on *:3000

On another machine on the same WiFi network, open a brower and type in the following (this assumes
that the raspberrypi IP addres is 192.168.0.8):

http://192.168.0.8:3000

In the page that is returned, you will see an input box and a 'send' button. Type something into the box
and click send. On the raspberrypi you should see printed out what you just typed in. 

Taking this code, you can develop it further to create a webbased keyboard with a bit of HTML, some images,
some CSS and a little bit more Javascript.

##python-sockets
Communicate over Wifi in Python!

### Setup
Ensure that you change the IP address to be correct. You will find this in keyboard.py on line 14:
    server_address = ('localhost', 10000)

In sock-server.py, you will find the IP address on line 5:
    server_address = ('localhost', 10000)

Run the server program first:
    python sock-server.py

If it runs correctly, it should say 'waiting for a connection'
Note that we run it with Python 2.7.x

Run the client program (in a different terminal window if testing, or on a different machine):

python keyboard.py

Now press the up, down left and right arrow keys.
Look at the server terminal window. It should contain something like the following messages:

    ('connection from', ('127.0.0.1', 59818))
    Received "U"
    Received "R"
    Received "D"
    Received "L"