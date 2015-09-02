var async = require('async');
var concatStream = require('concat-stream');
var fs = require('fs');
var http = require('http');

var file = process.argv[2];
async.waterfall([
  function(callback) {
    fs.readFile(file, function (error, data) {
      callback(error, data.toString());
    });
  },
  function(url, callback) {
    http.get(url, function (response) {
      response.setEncoding('utf8');
      response.pipe(concatStream(function (body) {
        callback(null, body);
      }));
    }).on('error', function (error) {
      callback(error);
    });
  },
], function(error, result) {
    if (error) {
      return console.error(error);
    }
    console.log(result);
});
