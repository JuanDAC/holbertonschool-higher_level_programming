#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  charPrint (c = 'X') {
    const character = c;
    const { width, height } = this;
    const shape = `${character.repeat(width)}\n`.repeat(height).slice(0, -1);
    console.log(shape);
  }
}

module.exports = Square;
