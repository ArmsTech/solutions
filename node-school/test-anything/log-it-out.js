var emotifyPath = process.argv[2];
var emotify = require(emotifyPath);
var stringToEmotify = process.argv[3];

console.log(emotify(stringToEmotify));
