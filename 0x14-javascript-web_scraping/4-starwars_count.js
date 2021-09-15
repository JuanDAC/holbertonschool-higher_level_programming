#!/usr/bin/node
const { get } = require('request');
const { argv } = require('process');
const url = argv[2];

get(url, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const { results } = JSON.parse(data);
  const count = [0, ...results]
    .reduce((prevr, { characters }) => prevr + [0, ...characters]
      .reduce((prevc, character) => prevc + character.includes('18')));
  console.log(isNaN(count) ? 0 : count);
});
