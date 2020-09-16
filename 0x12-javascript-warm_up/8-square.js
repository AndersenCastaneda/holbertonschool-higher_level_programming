#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
let msg = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      msg += 'X';
    }
    if (i < num - 1) {
      msg += '\n';
    }
  }
  console.log(msg);
}
