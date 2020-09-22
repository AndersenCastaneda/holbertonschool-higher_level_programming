#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let numberOfMovies = 0;
const id = '18';

if (url) {
  request(url, function getTitle (err, response, body) {
    if (!err) {
      const movies = JSON.parse(body).results;
      for (const movie of movies) {
        for (const character of movie.characters) {
          if (character.includes(id)) {
            numberOfMovies++;
          }
        }
      }
      console.log(numberOfMovies);
    }
  });
}
