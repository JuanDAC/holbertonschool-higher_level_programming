#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
}

module.exports = Rectangle;
