function every(array, f) {
  var isEvery = true;
  array.forEach(function(item) {
    if (!f(item))
      isEvery = false;
      return; // Exit forEach
  });
  return isEvery;
}

function some(array, f) {
  var isAny = false;
  array.forEach(function(item) {
    if (f(item))
      isAny = true;
      return; // Exit forEach
  });
  return isAny;
}

console.log(every([NaN, NaN, NaN], isNaN));
console.log(every([NaN, NaN, 4], isNaN));
console.log(some([NaN, 3, 4], isNaN));
console.log(some([2, 3, 4], isNaN));
