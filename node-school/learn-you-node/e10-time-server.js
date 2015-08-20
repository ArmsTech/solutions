var net = require('net');
var strftime = require('strftime');

var port = process.argv[2];

server = net.createServer(function (socket) {
  dateString = strftime('%Y-%m-%d %H:%M', new Date());
  socket.end(dateString);
});
server.listen(port);
