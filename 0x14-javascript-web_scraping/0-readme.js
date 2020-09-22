#!/usr/bin/node
const argv = process.argv.slice(2);
const fs = require('fs');
fs.readFile(argv[0], function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
