#!/usr/bin/node
const length = process.argv.slice(2).length;
const message = (length === 0) ? 'No argument'
  : (length === 1) ? 'Argument found' : 'Arguments found';
console.log(message);
