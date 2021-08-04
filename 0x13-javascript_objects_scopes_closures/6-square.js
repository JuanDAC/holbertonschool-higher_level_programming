#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    const character = c;
    const { width, height } = this;
    const shape = `${character.repeat(width)}\n`.repeat(height).slice(0, -1);
    console.log(shape);
  }
}

module.exports = Square;
