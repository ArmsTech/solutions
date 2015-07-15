function arrayToList(array) {
  var list, listHolder;
  for (var i = array.length - 1; i >= 0; i--) {
    // Inner-most item points to null
    listHolder = list || null;
    list = {
      value: array[i],
      rest: listHolder,
    };
  }
  return list || {};
}

function listToArray(list) {
  var array = [];
  for (var item = list; item; item = item.rest) {
    array.push(item.value);
  }
  return array;
}

function prepend(value, list) {
  var array = listToArray(list);
  array.unshift(value);
  return arrayToList(array);
}

function nth(list, index) {
  iteration = arguments.length === 3 ? arguments[2] : 0;
  if (index === iteration)
    return list.value;
  else if (list.rest === null)
    // Index not found
    return undefined;
  else
    return nth(list.rest, index, ++iteration);
}

console.log(arrayToList([10, 20]));
console.log(listToArray(arrayToList([10, 20, 30])));
console.log(prepend(10, prepend(20, null)));
console.log(nth(arrayToList([10, 20, 30]), 1));
