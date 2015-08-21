var http = require('http');
var through = require('through2');

var port = Number(process.argv[2]);
var transform = through(write);

function write (buffer, _, next) {
  this.push(buffer.toString().toUpperCase());
  next();
}

var server = http.createServer(function (request, response) {
    if (request.method === 'POST')
      request.pipe(transform).pipe(response);
    else
      response.end("Only accepting POST requests.\n");
});
server.listen(port);
