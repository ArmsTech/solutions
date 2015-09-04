var async = require('async');
var concatStream = require('concat-stream');
var http = require('http');
var querystring = require('querystring');

var url = process.argv[2];
async.reduce(['one', 'two', 'three'], 0,
  function(reduced, param, callback) {
    var urlWithParam = url + '/?' + querystring.stringify({number: param});
    http.get(urlWithParam, function (response) {
      response.setEncoding('utf8');
      response.pipe(concatStream(function (body) {
        callback(null, Number(body) + reduced);
      }));
    }).on('error', function (error) {
      callback(error);
    });
}, function(error, result){
    if (error) {
      return console.error(error);
    }
    console.log(result);
});
