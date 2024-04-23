#!/usr/bin/node

const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let output = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          output += c;
        }
        if (i !== this.width - 1) {
          output += '\n';
        }
      }
      console.log(output);
    }
  }
}
module.exports = Square;
