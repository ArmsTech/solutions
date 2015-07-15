function countBs(string) {
  return countChar(string, 'B');
}

function countChar(string, character) {
  var charsCounted = 0;

  for (var i = 0; i < string.length; i++) {
    if (string.charAt(i) === character)
      charsCounted++;
  }

  return charsCounted;
}

console.log(countBs("BBC"));
console.log(countChar("kakkerlak", "k"));
