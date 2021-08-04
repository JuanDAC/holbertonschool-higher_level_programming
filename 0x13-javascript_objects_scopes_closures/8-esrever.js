#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  list.forEach((value) => newList.shift(value));
  return (newList);
};
