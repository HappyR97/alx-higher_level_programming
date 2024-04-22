#!/usr/bin/node

const args = process.argv;
const iterations = Number(args[2]);

if (iterations) {
  for (let i = 0; i < iterations; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
