var through = require('through2');
var trumpet = require('trumpet');

var tr = trumpet();
var ws = tr.select('.loud').createStream();

ws.pipe(through(function (buffer, _, next) {
  this.push(buffer.toString().toUpperCase());
  next();
})).pipe(ws);

process.stdin.pipe(tr).pipe(process.stdout);
