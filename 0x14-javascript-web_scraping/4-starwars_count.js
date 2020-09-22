#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const characterID = 'https://swapi-api.hbtn.io/api/people/18/';
let numberOfMovies = 0;

request(url, function getTitle (err, response, body) {
  if (!err) {
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      const characters = movie.characters;
      if (characters.includes(characterID)) {
        numberOfMovies++;
      }
    }
    console.log(numberOfMovies);
  }
});
