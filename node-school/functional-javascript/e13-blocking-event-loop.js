function repeat(operation, number) {
  if (number <= 0) {
    return;
  }

  operation();

  if (number % 50 === 0) {
    setTimeout(function() {
      repeat(operation, --number);
    });
  } else {
      repeat(operation, --number);
  }
}

module.exports = repeat;
