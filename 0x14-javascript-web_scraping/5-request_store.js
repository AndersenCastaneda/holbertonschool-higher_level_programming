#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function getContent (err, response, body) {
  if (!err) {
    fs.writeFile(path, body, 'utf-8', function write (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
