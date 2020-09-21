#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    const msg = (c === undefined) ? 'X' : 'C';
    for (let i = 0; i < this.height; i++) {
      console.log(msg.repeat(this.width));
    }
  }
}

module.exports = Square;
