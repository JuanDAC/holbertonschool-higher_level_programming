#!/usr/bin/node

const { get } = require('request');
const { argv } = require('process');
const url = `https://swapi-api.hbtn.io/api/films/${argv[2]}`;

get(url, (err, { }, data) => {
  if (err) {
    return (console.log(err));
  }
  const { title } = JSON.parse(data);
  console.log(title);
});
