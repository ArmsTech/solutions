const MAX = +process.argv[2];
let FizzBuzz = {
  [Symbol.iterator]() {
    let number = 1;
    let value;
    return {
      next() {
        if (number > MAX) {
          return {done: true};
        }
        if (number % 3 === 0 && number % 5 === 0)
          value = "FizzBuzz";
        else if (number % 3 === 0)
          value = "Fizz";
        else if (number % 5 === 0)
          value = "Buzz";
        else
          value = number;
        number++;
        return {done: false, value: value};
      }
    };
  }
};

for (var n of FizzBuzz) {
  console.log(n);
}
