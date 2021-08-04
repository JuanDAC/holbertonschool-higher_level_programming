#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    const character = 'X';
    const { width, height } = this;
    const shape = `${character.repeat(width)}\n`.repeat(height).slice(0, -1);
    console.log(shape);
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
