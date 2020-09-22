#!/usr/bin/node
// Reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
