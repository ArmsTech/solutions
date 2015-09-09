var numbers = process.argv.slice(2);
var minimum = Math.min(...numbers);

console.log(`The minimum of [${numbers}] is ${minimum}`);
