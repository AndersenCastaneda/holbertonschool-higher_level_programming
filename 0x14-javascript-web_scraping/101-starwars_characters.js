#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');
const movieID = process.argv[2];

if (movieID) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;
  request(url, function taskCompleted (err, response, body) {
    if (!err) {
      const characters = JSON.parse(body).characters;
      for (const character in characters) {
        request(characters[character], function (err, response, body) {
          if (!err) {
            const info = JSON.parse(body);
            console.log(info.name);
          }
        });
      }
    }
  });
}
