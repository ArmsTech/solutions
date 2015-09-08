var _ = require("lodash");

var worker = function(comments) {
  return _.chain(comments)
      .groupBy('username')
      .map(function(group, username) {
        return {
          username: username,
          comment_count: _.size(group)};
      })
      .sortBy('comment_count').reverse();
};

module.exports = worker;
