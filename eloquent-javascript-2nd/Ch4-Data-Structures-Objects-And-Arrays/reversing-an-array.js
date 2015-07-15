function reverseArray(array) {
  reversed = [];
  for (var i = 0; i < array.length; i++) {
    reversed.unshift(array[i]);
  }
  return reversed;
}

function reverseArrayInPlace(array) {
  var holder, rightIndex;
  for (var i = 0; i < Math.floor(array.length / 2); i++) {
    // Left index will be i
    rightIndex = array.length - (i + 1);
    // Swap values to produce reverse effect
    holder = array[i];
    array[i] = array[rightIndex];
    array[rightIndex] = holder;
  }
}

console.log(reverseArray(["A", "B", "C"]));
var arrayValue = [1, 2, 3, 4, 5];
reverseArrayInPlace(arrayValue);
console.log(arrayValue);
