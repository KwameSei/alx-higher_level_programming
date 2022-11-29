#!/usr/bin/node
//class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const square = require('./5-square');

const Square = class Square extends square {
	charPrint (c) {
		if (c) {
			let display = '';
			for (let h1 = 0; h1 < this.height; h1++) {
				for (let w1 = 0; w1 < this.height; w1++) {
					display = display + c;
				}
				console.log(display);
				display = '';
			}
		} else {
			super.print();
		}
	}
};

module.exports = Square;
