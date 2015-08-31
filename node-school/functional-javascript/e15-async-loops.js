function loadUsers(userIds, load, done) {
  var users = userIds.map(function (userId) {
    return load(userId, function (user) {
      return user;
    });
  });
  done(users);
}

module.exports = loadUsers;
