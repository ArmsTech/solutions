var http = require('http');
var concatStream = require('concat-stream');

var counter = 0;
var results = Array(3);
var urls = process.argv.slice(2);

urls.forEach(function (url, index) {
  http.get(url, function (response) {
    response.setEncoding('utf8');
    response.pipe(concatStream(function (data) {
      results[index] = data;
      // Only log results when all gets are done
      if (++counter === 3)
        logResults(results);
    }));
  }).on('error', function (error) {
    console.error("Error encountered:", error);
  });
});

function logResults(results) {
  results.forEach(function (result) {
    console.log(result);
  });
}
