#!/usr/bin/node

// Parse all args to numbers and sort in desc order
const numbers = process.argv.slice(2).map(n => Number.parseInt(n));
numbers.sort((a, b) => b - a);

const secondMax = numbers.length > 1 ? numbers[1] : 0;

console.log(secondMax);
