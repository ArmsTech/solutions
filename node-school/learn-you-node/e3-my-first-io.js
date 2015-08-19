var fs = require('fs');

contents = fs.readFileSync(process.argv[2], 'utf8');
lines = contents.split('\n').length - 1;
console.log(lines);
