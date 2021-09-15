#!/usr/bin/node
const { get } = require('request');
const { argv } = require('process');

const number = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + number;

get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const { characters } = JSON.parse(body);

  characters.forEach(charUrl => get(charUrl, (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const { name } = JSON.parse(body);
    console.log(name);
  }));
});
