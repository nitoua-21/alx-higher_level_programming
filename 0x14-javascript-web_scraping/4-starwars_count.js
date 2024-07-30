#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
  } else {
    try {
      const films = JSON.parse(body).results;
      const wedgeFilms = films.filter(film =>
        film.characters.includes('Wedge Antilles')
      );
      console.log(wedgeFilms.length);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
