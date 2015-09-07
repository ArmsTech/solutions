var _ = require("lodash");

var worker = function(items) {
  return _.sortBy(items, 'quantity').reverse();
};

module.exports = worker;
