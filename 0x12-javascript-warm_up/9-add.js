#!/usr/bin/node
const argv = require('process').argv;

const operator = parseInt(Number(argv[3]));
const operating = parseInt(Number(argv[2]));

if (isNaN(operator) || isNaN(operating)) {
  console.log('NaN');
} else {
  console.log(operating + operator);
}
