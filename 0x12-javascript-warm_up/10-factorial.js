#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
function factorial (num) {
  if (num === 1) {
    return num;
  }
  const rec = factorial(num - 1);
  return num * rec;
}
console.log((isNaN(a) || a <= 1) ? 1 : factorial(a));
