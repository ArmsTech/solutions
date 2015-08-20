var fs = require('fs');
var http = require('http');

var port = Number(process.argv[2]);
var file = process.argv[3];

http.createServer(function (request, response) {
  fs.createReadStream(file).pipe(response);
}).listen(port);
