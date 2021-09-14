#!/usr/bin/node

const { get } = require('request');
const { argv } = require('process');
const url = argv[2];

get(url, (err, { statusCode }, body) => {
  if (err) {
    return (console.log(err));
  }
  console.log(`code: ${statusCode}`);
});
