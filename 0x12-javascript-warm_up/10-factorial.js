#!/usr/bin/node
// Computes and prints the factorial of a given number.

const { argv } = require('process');

const number = parseInt(argv[2]);

// Define recursive factorial function.
const factorial = number => {
  if (number === 0) {
    return (1);
  }

  return (number * factorial(number - 1));
};

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
