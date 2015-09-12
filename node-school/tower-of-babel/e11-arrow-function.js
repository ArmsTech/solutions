var inputs = process.argv.slice(2);
var result = inputs
  .map((input) => input[0])
  .reduce((reduced, character) => reduced + character);

console.log(result);
