var through = require('through2');
var transform = through(write);

function write (buffer, encoding, next) {
    this.push(buffer.toString().toUpperCase());
    next();
}

process.stdin.pipe(transform).pipe(process.stdout);
