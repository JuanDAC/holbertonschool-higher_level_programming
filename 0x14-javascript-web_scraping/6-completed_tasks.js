#!/usr/bin/node

const { get } = require('request');
const { writeFile } = require('fs');
const { argv } = require('process');

const url = argv[2];
const filename = argv[3];

get(url, (err, res, body) => {
  if (err) {
    console.log(err)
    return;
  }

  const data = JSON.parse(body);
  const tasks = {};

  data.forEach(({completed, userId: id}) => {
    if (completed) {
      tasks[id] = 1 + (tasks[id] == undefined ? 0 : tasks[id])
    }
  });
  console.log(tasks);
});
