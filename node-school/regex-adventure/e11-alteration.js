module.exports = function (string) {
  return /\b(cat|dog|robot)\d+$/.test(string);
};
