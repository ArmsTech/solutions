function repeat(operation, num) {
  if (num > 0) {
    operation();
    return repeat(operation, --num);
  }
}

module.exports = repeat;
