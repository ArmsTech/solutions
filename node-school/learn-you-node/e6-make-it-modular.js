var extfilter= require('extfilter');

var directory = process.argv[2];
var extension = process.argv[3];

extfilter(directory, extension, function (error, files) {
  if (error)
    return console.error("Error encountered:", error);
  files.forEach(function (file) {
    console.log(file);
  });
});
