var repeatCallback = require(process.argv[2]);
var tape = require('tape');

tape('Testing repeatCallback.', function(test) {
  test.plan(5);
  repeatCallback(5, function() {
    test.pass('Callback called.');
  });
});
