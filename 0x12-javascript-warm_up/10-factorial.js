#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
if (isNaN(a)) {
  console.log(1);
} else {
  let x = 1;
  for (let i = a; i > 1; i--) {
    x *= i;
  }
  console.log(x);
}
