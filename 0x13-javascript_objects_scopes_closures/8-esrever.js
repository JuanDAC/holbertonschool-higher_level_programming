#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 1) {
    return ([list.pop()]);
  }
  return [list.pop()].concat(exports.esrever(list));
};
