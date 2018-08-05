// Create all the variables/objects you need
// Express is the web application framework
var express = require('express');
// The express application
var app = express();
// The file path
var path = require('path');
// The web server
var server = require('http').Server(app);
// The web server socket
var io = require('socket.io')(server);

// Sets the 'public' folder to be the root from where js & css resources are served
app.use(express.static(path.join(__dirname, 'public')));

// When a client connects, this callback function is called
io.on('connection', function (socket) {
    console.log('a user connected');

    // Sets up an event after the user has connected to listen for data being sent by the client
    socket.on('sending', function (data) {
        // Log the data sent so you can see it on the console
        console.log(data);

        // Provides the client a way of disconnecting from the server
        if (data == "x") {
            socket.disconnect(console.log('sender disconnected'));
        }
    });
});

// index.html is sent to the user when requested in the browser
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

// listen for connections
server.listen(3000, function () {
    console.log('listening on *:3000');
});