var ancestry = JSON.parse(require('./ancestry.js'));

function average(array) {
  function plus(a, b) { return a + b; }
  return array.reduce(plus) / array.length;
}

var byName = {};
ancestry.forEach(function(person) {
  byName[person.name] = person;
});

/* Find the age difference between a person and their mother. Then, filter
 * out cases where a person's mother was not found in the ancestry tree. */
var ageDifference = ancestry.map(function(person) {
  if (person.mother in byName) {
    return person.born - byName[person.mother].born;
}}).filter(function(person) {if (person) return person;});

console.log(average(ageDifference));
