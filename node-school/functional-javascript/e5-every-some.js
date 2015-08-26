function checkUsersValid(goodUsers) {
  return function allUsersValid(submittedUsers) {
    return submittedUsers.every(function (submittedUser) {
      return goodUsers.some(function (goodUser) {
        return submittedUser.id === goodUser.id;
      });
    });
  };
}

module.exports = checkUsersValid;
