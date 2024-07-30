#!/usr/bin/node

const request = require('request');

// Get the URL from command line arguments
const url = process.argv[2];

// Make a GET request
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
