#!/usr/bin/node
const { argv } = require('process');
console.log(argv[2] ? `${argv[2]}` : 'No argument');
