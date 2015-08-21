var split = require('split');
var through = require('through2');

var lineNumber = 1;
var transform = through(write);

function write (buffer, _, next) {
  line = buffer.toString();
  line = (lineNumber++ % 2 === 0) ? line.toUpperCase() : line.toLowerCase();
  this.push(line + '\n');
  next();
}

process.stdin.pipe(split()).pipe(transform).pipe(process.stdout);
