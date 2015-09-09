module.exports = function makeImportant(text, importance = text.length) {
  return text + '!'.repeat(importance);
};
