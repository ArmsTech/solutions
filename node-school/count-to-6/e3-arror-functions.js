var inputs = process.argv.slice(2);
var result = inputs
  .map(input => input.charAt(0))
  .reduce((reduced, character) => reduced + character);

console.log(`[${inputs}] becomes "${result}"`);
