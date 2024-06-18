#!/usr/bin/node

const firstArg = Number.parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArg);
}
