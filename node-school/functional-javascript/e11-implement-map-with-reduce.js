module.exports = function arrayMap(arr, fn) {
  return arr.reduce(function (maps, current, index, array) {
    maps.push(fn(current));
    return maps;
  }, []);
};
