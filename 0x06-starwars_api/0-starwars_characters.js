const request = require(`request`);

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character details:', error);
        }
      });
    });
  } else {
    console.error('Error fetching movie details:', error);
  }
});
