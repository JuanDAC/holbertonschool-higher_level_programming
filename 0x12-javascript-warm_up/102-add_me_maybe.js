#!/usr/bin/node

function callMeMoby (number, theFunction) {
  theFunction(number + 1);
}

exports.callMeMoby = callMeMoby;
