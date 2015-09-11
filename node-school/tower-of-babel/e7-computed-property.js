// This code isn't very readable, but the exercise asked for it.
console.log({
  [+process.argv[2] % 2 === 0 ? "even" : "odd"]: +process.argv[2],
  [+process.argv[3] + +process.argv[2]]: +process.argv[3] + +process.argv[2]
});
