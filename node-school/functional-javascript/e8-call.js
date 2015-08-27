function duckCount() {
  var ducks = Array.prototype.slice.call(arguments);
  return ducks.filter(function (duck) {
    return Object.prototype.hasOwnProperty.call(duck, 'quack');
  }).length;
}

module.exports = duckCount;
