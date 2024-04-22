#!/usr/bin/node

const args = process.argv;

function factorial (a) {
  if (a === 0 || a === 1 || isNaN(a)) {
    return 1;
  } else {
    a *= factorial(a - 1);
  }
  return a;
}

console.log(factorial(Number(args[2])));
