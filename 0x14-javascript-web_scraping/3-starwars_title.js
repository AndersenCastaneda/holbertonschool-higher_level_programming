#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;

request(url, function getTitle (err, response, body) {
  if (!err) {
    const ep = JSON.parse(body);
    console.log(ep.title);
  }
});
