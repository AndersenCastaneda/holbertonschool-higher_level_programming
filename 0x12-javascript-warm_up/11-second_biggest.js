#!/usr/bin/node
let secBig = 0;
const argv = process.argv.slice(2);
if (argv.length > 1) {
  argv.sort();
  for (let i = argv.length - 1; i > 0; i--) {
    if (argv[i] > argv[i - 1]) {
      secBig = argv[i - 1];
      break;
    }
  }
}
console.log(secBig);
