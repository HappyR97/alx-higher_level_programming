#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);

if (isNaN(args[2]) || args.length === 1) {
  console.log(0);
} else {
  const sorted = numbers.sort((a, b) => b - a);
  console.log(sorted[1]);
}
