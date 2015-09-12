function getDependencies(tree, result) {
  result = result || [];
  var dependencies = tree && tree.dependencies || [];

  Object.keys(dependencies).forEach(function(dependency) {
    var key = dependency + '@' + tree.dependencies[dependency].version;
    if (result.indexOf(key) === -1) {
      result.push(key);
    }
    getDependencies(tree.dependencies[dependency], result);
  });

  return result.sort();
}

module.exports = getDependencies;
