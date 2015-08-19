var fs = require('fs');
var path = require('path');

var directory = process.argv[2];
var extension = '.' + process.argv[3];

fs.readdir(directory, function (error, files) {
  if (error)
    throw error;
  // Files with matching extension
  var matches = files.filter(function (file) {
    return path.extname(file) === extension;
  });
  matches.forEach(function (match) {
    console.log(match);
  });
});
