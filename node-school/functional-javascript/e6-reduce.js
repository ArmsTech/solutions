function countWords(inputWords) {
  return inputWords.reduce(function (counts, word) {
    if (word in counts)
      counts[word]++;
    else
      counts[word] = 1;
    return counts;
  }, {});
}

module.exports = countWords;
