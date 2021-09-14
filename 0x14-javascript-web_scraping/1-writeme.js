#!/usr/bin/node

const { argv } = require('process');
const { writeFile } = require('fs');
const filename = argv[2];
const content = argv[3];

try {
  writeFile(filename, content, err => {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
