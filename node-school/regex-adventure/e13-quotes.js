module.exports = function (string) {
  return string.match(/"[^"]*"/g)
}
