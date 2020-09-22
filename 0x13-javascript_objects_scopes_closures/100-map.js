#!/usr/bin/node
const list = require('./100-data').list;

const res = [];
list.map((value, index) => res.push(value * index));
console.log(list);
console.log(res);
