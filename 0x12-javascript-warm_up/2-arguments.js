#!/usr/bin/node
const argv = require('process').argv;

console.log((argv.length > 1) ? 'Argument found' : 'No argument');
