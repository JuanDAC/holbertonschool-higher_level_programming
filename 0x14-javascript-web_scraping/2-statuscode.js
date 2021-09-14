#!/usr/bin/node

const { get: GET } = require('request');
const { argv: [_one, _two, url] } = require('process');

GET(url, (err, { statusCode }, body) => {
  if (err) {
    return (console.log(err));
  }
  console.log(`code: ${ statusCode }`);
});

