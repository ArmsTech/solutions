var async = require('async');
var concatStream = require('concat-stream');
var http = require('http');

var count = 0;
var foundMeerkat = false;
var url = process.argv[2];

async.whilst(
    function () { return !foundMeerkat; },
    function (callback) {
      http.get(url, function (response) {
        response.setEncoding('utf8');
        response.pipe(concatStream(function (body) {
          count++;
          foundMeerkat = body.indexOf('meerkat') > -1;
          callback();
        }));
      }).on('error', function (error) {
        callback(error);
      });
    },
    function (error) {
      console.log(count);
    }
);
