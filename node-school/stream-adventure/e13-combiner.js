var combine = require('stream-combiner');
var split = require('split');
var through = require('through2');
var zlib = require('zlib');

module.exports = function () {
  var genre = {};

  function write (buffer, _, next) {
    try {
      json = JSON.parse(buffer);
    } catch (error) {
      return next();
    }

    if (json.type === 'genre') {
      if (Object.keys(genre).length !== 0)
        this.push(JSON.stringify(genre) + '\n');
      genre = {'name': json.name, 'books': []};
    } else
        genre.books.push(json.name);

    next();
  }

  function end (done) {
      this.push(JSON.stringify(genre) + '\n');
      this.push(null);
      done();
  }

  return combine(split(), through(write, end), zlib.createGzip());
};
