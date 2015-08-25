var concat = require('concat-stream');
var crypto = require('crypto');
var tar = require('tar');
var zlib = require('zlib');

var parser = tar.Parse();
parser.on('entry', function (file) {
    if (file.type === "File")
      file.pipe(concat(function (data) {
        hash = crypto.createHash('md5').update(data).digest('hex');
        console.log(hash + ' ' + file.path);
      }));
});

var cipher = process.argv[2];
var passphrase = process.argv[3];
var decrypted = crypto.createDecipher(cipher, passphrase);

process.stdin.
  pipe(decrypted).
  pipe(zlib.createGunzip()).
  pipe(parser)
;
