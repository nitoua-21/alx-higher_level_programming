#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
  } else {
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      }
    });
  }
});
