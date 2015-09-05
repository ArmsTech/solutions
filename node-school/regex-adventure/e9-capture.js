module.exports = function (string) {
  var match = /x=(\d+)/.exec(string)
  return match ? match[1] : null
}
