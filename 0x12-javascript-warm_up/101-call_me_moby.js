#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  Array.apply([], Array(x)).forEach(() => theFunction());
};

exports.callMeMoby = callMeMoby;
