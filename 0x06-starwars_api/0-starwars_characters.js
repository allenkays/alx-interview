#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    const fetchCharacterData = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            reject(new Error('Error fetching character details'));
          }
        });
      });
    };

    Promise.all(characters.map(fetchCharacterData))
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error);
      });
  } else {
    console.error('Error fetching movie details:', error);
  }
});
