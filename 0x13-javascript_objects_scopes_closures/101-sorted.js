#!/usr/bin/node
const { dict } = require('./101-data.js');

const occurrencesById = dict;
const idsByOccurrence = {};

for (const [userId, occurrence] of Object.entries(occurrencesById)) {
  if (!idsByOccurrence[occurrence]) {
    idsByOccurrence[occurrence] = [];
  }
  idsByOccurrence[occurrence].push(userId);
}

console.log(idsByOccurrence);
