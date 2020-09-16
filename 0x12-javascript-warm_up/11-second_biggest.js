#!/usr/bin/node
const argv = process.argv.slice(2);
const length = argv.length;
if (length === 0 || length === 1) {
  console.log(0);
} else {
  let arr = argv.sort();
  console.log(arr[length - 2]);
}
