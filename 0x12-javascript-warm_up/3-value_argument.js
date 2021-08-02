#!/usr/bin/node
const argv = require('process').argv;

console.log((argv.length > 2) ? argv[2] : 'No argument');
