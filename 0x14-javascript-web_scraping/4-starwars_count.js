#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let numberOfMovies = 0;
const id = 'https://swapi-api.hbtn.io/api/people/18';

if (url) {
  request(id, function getTitle (err, response, body) {
    if (!err) {
      const films = JSON.parse(body).films;
      console.log(films.length);
    }
  });
}
