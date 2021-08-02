#!/usr/bin/node
const argv = require('process').argv;

const number = parseInt(Number(argv[2]));

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
}
