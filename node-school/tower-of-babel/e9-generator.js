const MAX = +process.argv[2];

let fizzBuzz = function*(){
  let number = 1;
  let value;

  while (number <= MAX) {
    if (number % 3 === 0 && number % 5 === 0)
      value = "FizzBuzz";
    else if (number % 3 === 0)
      value = "Fizz";
    else if (number % 5 === 0)
      value = "Buzz";
    else
      value = number;

    number++;
    yield value;
  }
}();

for (var n of fizzBuzz) {
  console.log(n);
}
