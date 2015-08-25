var duplexer2 = require('duplexer2');
var stream = require("stream");

module.exports = function (counter) {
  var writable = new stream.Writable({objectMode: true});
  writable.counts= {};

  writable._write = function _write(data, _, done) {
    if (!(data.country in this.counts))
      this.counts[data.country] = 0;
    this.counts[data.country]++;
    done();
  };

  writable.on('finish', function () {
    counter.setCounts(this.counts);
  });

  return duplexer2(writable, counter);
};
