function repeat(operation, number) {
  return function() {
    if (number <= 0) {
      return undefined;
    }
    operation();
    return repeat(operation, --number);
  };
}

function trampoline(fn) {
  while (fn) {
    fn = fn();
  }
}

module.exports = function(operation, number) {
  return trampoline(repeat(operation, number));
};
