#!/usr/bin/node
const argv = process.argv.slice(2);
console.log((argv[0] === undefined) ? 'undefined is undefined'
  : (argv[1] === undefined) ? `${argv[0]} is undefined` : `${argv[0]} is ${argv[1]}`);
