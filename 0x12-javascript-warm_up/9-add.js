#!/usr/bin/node

const add = (a, b) => (a + b);
const firstInt = Number.parseInt(process.argv[2]);
const secondInt = Number.parseInt(process.argv[3]);

console.log(add(firstInt, secondInt));
