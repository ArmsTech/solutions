var _ = require("lodash");

var worker = function(users) {
  return _.where(users, {'active': true});
};

module.exports = worker;
