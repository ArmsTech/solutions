var _ = require("lodash");

var worker = function(towns) {
  var everyHot = false;
  var groups = {hot: [], warm: []};
  var someHot = false;

  function checkHotness(temp) {
    return temp > 19;
  }

  _.forEach(towns, function(town, townName) {
    // Is every town hot?
    everyHot = _.every(towns[townName], checkHotness);
    if (everyHot) {
      groups.hot.push(townName);
    } else {
      // Are some (at least 1) of the towns hot?
      someHot = _.some(towns[townName], checkHotness);
      if (someHot) {
        groups.warm.push(townName);
      }
    }
  });

  return groups;
};

module.exports = worker;
