#!/usr/bin/node
// Creating an empty rectangle
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		let display = '';
		for (let h1 = 0; h1 < this.height; h1++){
			for (let w1 = 0; w1 < this.width; w1++) {
				display = display + 'X';
			}
			console.log(display);
			display = '';
		}
	}
};


module.exports = Rectangle;
