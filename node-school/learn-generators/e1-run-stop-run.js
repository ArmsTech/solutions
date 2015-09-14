function *range(from, to) {
  while (from <= 10)
    yield from++;
}

for (var r of range(5, 10)) {
    console.log(r);
}
