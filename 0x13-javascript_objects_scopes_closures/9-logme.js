#!/usr/bin/node

exports.logMe = ((counter = 0) => function (item) {
  console.log(`${counter++}: ${item}`);
})();
