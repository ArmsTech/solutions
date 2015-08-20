var http = require('http');
var url = require('url');

var port = Number(process.argv[2]);

http.createServer(function (request, response) {
  parsedURL = url.parse(request.url, true);
  date = new Date(parsedURL.query.iso);

  switch (parsedURL.pathname) {
    case '/api/parsetime':
      response.writeHead(200, {'Content-Type': 'application/json'});
      response.end(JSON.stringify({
        'hour': date.getHours(),
        'minute': date.getMinutes(),
        'second': date.getSeconds()
      }));
      break;
    case '/api/unixtime':
      response.writeHead(200, {'Content-Type': 'application/json'});
      response.end(JSON.stringify({
        'unixtime': new Date(date.toISOString()).getTime()
      }));
      break;
    default:
      response.writeHead(404);
      response.end();
  }
}).listen(port);
