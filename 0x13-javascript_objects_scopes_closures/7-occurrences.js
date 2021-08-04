#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return ([0, ...list].reduce((acum, current) => acum + (current === searchElement)));
};
