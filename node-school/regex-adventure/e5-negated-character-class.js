module.exports = function (string) {
  return /^[\D][^A-Z]/.test(string);
};
