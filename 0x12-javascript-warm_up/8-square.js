#!/usr/bin/node

const args = process.argv;
const size = Number(args[2]);
let output = '';

if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      output += 'X';
    }
    if (i !== size - 1) {
      output += '\n';
    }
  }
  console.log(output);
} else {
  console.log('Missing size');
}
