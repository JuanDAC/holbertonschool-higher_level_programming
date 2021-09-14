#!/usr/bin/node

const {get: GET} = require('request');
const { argv: [_, _, url] } = require('process');

GET(url, (err, response, body) => {
  if (err) {
    return (console.log(err));
  }
  console.log('code: ' + response.statusCode);
});

