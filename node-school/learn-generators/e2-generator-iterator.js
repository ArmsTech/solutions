function *factorial(number) {
  var result = 1;
  for (var i = 1; i <= number; i++) {
      result *= i;
      yield result;
  }
}

for (var number of factorial(5)) {
  console.log(number);
}
