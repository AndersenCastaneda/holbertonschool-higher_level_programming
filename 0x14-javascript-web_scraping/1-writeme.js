#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 2) {
  const fs = require('fs');
  fs.writeFile(argv[0], argv[1], (err) => {
    if (err) {
      console.log(err);
    }
  });
}
