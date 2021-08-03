#!/usr/bin/node

const callMeMoby = (x, theFunction) => Array.apply([], Array(x)).forEach(theFunction);

exports.callMeMoby = callMeMoby;
