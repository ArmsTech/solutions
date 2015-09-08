var _ = require("lodash");

var worker = function(user) {
  return _.template("Hello <%= name %> (logins: <%= login %>)")({
    name: user.name,
    login: _.size(user.login)
  });
};

module.exports = worker;
