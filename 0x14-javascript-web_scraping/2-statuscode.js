#!/usr/bin/node

const { get: GET } = require('request');
const { argv } = require('process');
const url = argv[2];

GET(url, (err, { statusCode }, body) => {
  if (err) {
    return (console.log(err));
  }
  console.log(`code: ${statusCode}`);
});
