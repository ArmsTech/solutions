function deepEqual(first, second) {
  if (first === null || second === null)
    return first === second;
  else if (typeof first === 'object' && typeof second === 'object') {
    var keys = Object.keys(first).concat(Object.keys(second));
    var keysCompared = [];

    for (var i = 0; i < keys.length; i++) {
      // Ignore duplicates
      if (keysCompared.indexOf(keys[i]) !== -1) continue;
      keysCompared.push(keys[i]);

      if (!deepEqual(first[keys[i]], second[keys[i]]))
        return false;
    }
      // All object attributes were equal
      return true;
  } else
      return first === second;
}

var obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
console.log(deepEqual(obj, {here: 1, object: 2}));
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
