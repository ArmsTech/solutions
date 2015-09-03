var async = require('async');
var concatStream = require('concat-stream');
var http = require('http');

var urlOne = process.argv[2];
var urlTwo = process.argv[3];

function getURL(url, callback) {
  http.get(url, function (response) {
    response.setEncoding('utf8');
    response.pipe(concatStream(function (body) {
      callback(null, body);
    }));
  }).on('error', function (error) {
    callback(error);
  });
}

async.series({
  requestOne: function(callback) {
    getURL(urlOne, callback);
  },
  requestTwo: function(callback) {
    getURL(urlTwo, callback);
  }
}, function(error, results) {
    if (error) {
      return console.error(error);
    }
    console.log(results);
});
