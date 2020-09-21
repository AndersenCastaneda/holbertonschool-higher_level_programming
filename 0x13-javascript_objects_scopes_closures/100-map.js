#!/usr/bin/node
let list = require('./100-data.js').list;
console.log(list);
list = list.map(x => x * list.indexOf(x));
console.log(list);
