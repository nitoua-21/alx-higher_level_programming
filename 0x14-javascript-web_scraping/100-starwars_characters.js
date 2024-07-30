#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the movie
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to get character name from URL
function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) reject(error);
      else if (response.statusCode !== 200) reject(new Error(`Invalid status code: ${response.statusCode}`));
      else resolve(JSON.parse(body).name);
    });
  });
}

// Make a GET request to the movie API
request(movieUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
  } else {
    try {
      const movie = JSON.parse(body);
      for (const characterUrl of movie.characters) {
        try {
          const name = await getCharacterName(characterUrl);
          console.log(name);
        } catch (characterError) {
          console.error('Error fetching character:', characterError);
        }
      }
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
