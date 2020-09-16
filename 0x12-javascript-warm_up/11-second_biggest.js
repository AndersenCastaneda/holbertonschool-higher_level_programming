#!/usr/bin/node
const argv = process.argv.slice(2);
function comp (a, b) {
  return a - b;
}
console.log((argv.length === 0 || argv.length === 1) ? 0
  : argv.sort(comp)[argv.length - 2]);
