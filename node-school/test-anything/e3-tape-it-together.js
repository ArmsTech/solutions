var fancify = require(process.argv[2]);
var tape = require('tape');

tape('Testing fancify.', function (test) {
  test.strictEqual(fancify('Hello'), '~*~Hello~*~');
  test.strictEqual(fancify('Hello', true), '~*~HELLO~*~');
  test.strictEqual(fancify('Hello', false, '!'), '~!~Hello~!~');
  test.end();
});
