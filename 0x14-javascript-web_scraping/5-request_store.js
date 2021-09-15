#!/usr/bin/node
const { get } = require('request');
const { writeFile } = require('fs');
const { argv } = require('process');

const url = argv[2];
const filename = argv[3];

get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  writeFile(filename, body, 'utf8', err => {
    if (err) {
      console.log(err);
    }
  });
});
