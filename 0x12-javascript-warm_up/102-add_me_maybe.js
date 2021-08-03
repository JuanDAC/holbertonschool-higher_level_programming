#!/usr/bin/node

const callMeMoby = function (number, theFunction) {
  theFunction(number + 1);
};

exports.callMeMoby = callMeMoby;
