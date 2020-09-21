#!/usr/bin/node
let i = 0;
const list = require('./100-data.js').list;
const res = list.map(x => x * i++);
console.log(list);
console.log(res);
