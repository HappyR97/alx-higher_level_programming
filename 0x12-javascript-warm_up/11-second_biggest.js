#!/usr/bin/node

const args = process.argv.splice(2);
const numbers = args.map(Number);

if (isNaN(args[2]) || args[2] === 1) {
  console.log(0);
} else {
  const sorted = numbers.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
