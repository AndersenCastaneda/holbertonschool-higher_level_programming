#!/usr/bin/node
// Displays the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, function getUrl (err, response) {
  console.log((!err) ? `code: ${response.statusCode}` : err);
});
