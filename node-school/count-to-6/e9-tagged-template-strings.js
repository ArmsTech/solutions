var ESCAPES = {
  '&': '&amp;',
  "'": '&apos;',
  '"': '&quot;',
  '<': '&lt;',
  '>': '&gt;'
};

function html(strings, ...substitutions) {
  var re;
  var substituted = substitutions.map(function(substitution) {
    for (var escapeChar in ESCAPES) {
      re = new RegExp(`${escapeChar}`, "g");
      substitution = substitution.replace(re, ESCAPES[escapeChar]);
    }
    return substitution;
  });

  return strings.reduce(function(reduced, current, index) {
    reduced += current;
    if (index < substituted.length) {
      reduced += substituted[index];
    }
    return reduced;
    }, '');
}

console.log(html`<b>${process.argv[2]} says</b>: "${process.argv[3]}"`);
