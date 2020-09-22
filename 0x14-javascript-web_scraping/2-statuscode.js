#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
if (url !== undefined) {
  request
    .get(url)
    .on('error', function (err) {
      console.error(err);
    })
    .on('response', function (response) {
      console.log(response.statusCode);
    });
}
