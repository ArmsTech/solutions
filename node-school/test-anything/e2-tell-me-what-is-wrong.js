var assert = require('assert');
var isCoolNumber = require(process.argv[2]);

assert.strictEqual(
  isCoolNumber(42), true, 'isCoolNumber(42) should be true');
