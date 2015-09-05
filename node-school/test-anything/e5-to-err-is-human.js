var feedCat = require(process.argv[2]);
var tape = require('tape');

tape('Testing feedCat.', function(test) {
  test.plan(2);
  test.equals(feedCat('fish'), 'yum');
  test.throws(function() {
    feedCat('chocolate');
  });
});
