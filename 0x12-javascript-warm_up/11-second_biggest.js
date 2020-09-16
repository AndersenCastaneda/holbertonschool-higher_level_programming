#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 0 || argv.length === 1) {
  console.log(0);
} else {
  const arr = argv.sort();
  console.log(arr[argv.length - 2]);
}
