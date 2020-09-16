#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);
console.log((isNaN(a) || isNaN(b) ? 'NaN' : a + b));
