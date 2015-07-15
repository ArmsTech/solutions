var ancestry = JSON.parse(require('./ancestry.js'));

function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

function groupBy(array, grouper) {
  groupedItems = {};
  array.forEach(function(item) {
    groupedItem = grouper(item);
    if (groupedItem in groupedItems)
      groupedItems[groupedItem].push(item);
    else
      groupedItems[groupedItem] = [item];
  });
  return groupedItems;
}

function getAges(persons) {
  var ages = [];
  persons.forEach(function(person) {
    ages.push(person.died - person.born);
  });
  return ages;
}

// Get all persons grouped by century
var byCentury = groupBy(ancestry, function(person) {
  return Math.ceil(person.died / 100);
});

// For all persons grouped by century, print the average age
var averageAge;
for (var century in byCentury) {
  // Fix to 1 decimal place (no rounding)
  averageAge = average(getAges(byCentury[century])).toFixed(1);
  console.log(century, ':', averageAge);
}
