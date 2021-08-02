#!/usr/bin/node
// Computes and prints the factorial of a given number.

const { argv } = require('process');

const penultimate = argv.slice(2)
  .sort((a, b) => b - a)
  .filter((item, index, array) => array.indexOf(item) === index)[1];

console.log(penultimate || 0);
