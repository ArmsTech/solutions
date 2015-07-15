function range(start, end, step) {
  var array = [], action = "push";
  if (step === undefined)
    step = start <= end ? 1 : -1;

  /* Handle negative ranges by swapping start and end, stepping positively,
   * and inserting range numbers instead of pushing them. */
  if (start > end) {
    // Swap variables in a horrific but one-line way
    end = [start, start = end][0];
    action = "unshift";
    step = Math.abs(step);
  }

  for (var i = start; i <= end; i += step) {
    array[action](i);
  }
  return array;
}

function sum(numbers) {
  var result = 0;
  for (var i = 0; i < numbers.length; i++) {
    result += numbers[i];
  }
  return result;
}

console.log(sum(range(1, 10)));
console.log(range(1, 10, 2));
console.log(range(5, 2, -1));
