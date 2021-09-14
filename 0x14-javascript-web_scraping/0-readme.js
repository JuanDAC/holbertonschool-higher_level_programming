#!/usr/bin/node

const { argv } = require('process');
const { readFile } = require('fs');
const filename = argv[2];

try {
  readFile(filename, (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data.toString('utf8'));
    }
  });
} catch (err) {
  console.log(err);
}


