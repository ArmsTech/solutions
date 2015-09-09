module.exports = function average(...numbers) {
  return numbers
    .reduce((reduced, number) => reduced + number, 0) / numbers.length;
};
