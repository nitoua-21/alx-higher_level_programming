#!/usr/bin/node

const oldList = require('./100-data.js').list;

const newList = oldList.map((idx, item) => idx * item);

console.log(oldList);
console.log(newList);
