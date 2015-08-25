var spawn = require('child_process').spawn;
var duplexer = require('duplexer');

module.exports = function (cmd, args) {
  spawned = spawn(cmd, args);
  return duplexer(spawned.stdin, spawned.stdout);
};
