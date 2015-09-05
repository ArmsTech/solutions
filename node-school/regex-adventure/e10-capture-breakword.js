module.exports = function (string) {
  var match = /\bx=(\d+)\b/.exec(string)
  return match ? match[1] : null
}
