var async = require('async');
var concatStream = require('concat-stream');
var http = require('http');
var querystring = require('querystring');

var hostname = process.argv[2];
var port = Number(process.argv[3]);
var options = {
  host: hostname,
  path: '/users/create',
  port: port,
  method: 'POST'
};

function createUser(userId, callback) {
  var data = JSON.stringify({'user_id': userId});
  options.headers = {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(data)
  };

  var request = http.request(options, function(response) {
    response.setEncoding('utf8');
  });
  request.on('error', function(error) {
    callback(error);
  });
  request.write(data);
  request.end(callback(null));
}

async.series({
  post: function(callback) {
    async.times(5, function(number, next){
      createUser(number + 1, next);
    });
    callback(null);
  },
  get: function(callback) {
    var url = 'http://' + hostname + ':' + port + '/users';
    http.get(url, function (response) {
      response.setEncoding('utf8');
      response.pipe(concatStream(function (body) {
        callback(null, body);
      }));
    }).on('error', function (error) {
      callback(error);
    });
  }
}, function(error, results){
    if (error) {
      return console.error(error);
    }
    console.log(results.get);
});
