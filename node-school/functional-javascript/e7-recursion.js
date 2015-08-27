function reduce(array, fn, initial, index) {
  index = index || 0;
  if (index === array.length) {
    return initial;
  }
  return reduce(
    array,
    fn,
    fn(initial, array[index], index, array),
    ++index
  );
}

module.exports = reduce;
