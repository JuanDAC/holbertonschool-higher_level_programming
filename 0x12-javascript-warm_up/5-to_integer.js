#!/usr/bin/node
const argv = require('process').argv;

const number = parseInt(Number(argv[2]));

console.log(isNaN(number) ? 'Not a number' : `My number: ${number}`);
