#!/usr/bin/node
'use strict';
let secBig = 0;
let argv = process.argv.slice(2);
if (argv.length > 1) {
  argv.sort();
  secBig = argv[argv.length - 2];
}
console.log(secBig);
