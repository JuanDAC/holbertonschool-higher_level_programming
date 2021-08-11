#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 1) {
    return ([list.pop()]);
  }
  if (list.length === 0) {
    return ([]);
  }
  return [list.pop()].concat(exports.esrever(list));
};
