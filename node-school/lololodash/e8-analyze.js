var _ = require("lodash");

var worker = function(freeLancers) {
  var result = {};
  var totalIncome = _.reduce(freeLancers, function(total, freeLancer) {
    return total + freeLancer.income;
  }, 0);

  result.average = totalIncome / _.size(freeLancers);

  result.underperform = _.chain(freeLancers)
    .filter(function(freeLancer) {
      return freeLancer.income <= result.average;
    })
    .sortBy('income');

  result.overperform = _.chain(freeLancers)
    .filter(function(freeLancer) {
      return freeLancer.income > result.average;
    })
    .sortBy('income');

  return result;
};

module.exports = worker;
