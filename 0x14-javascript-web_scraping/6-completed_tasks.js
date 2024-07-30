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
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
