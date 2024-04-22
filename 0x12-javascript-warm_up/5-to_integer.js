#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);

if (num) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
