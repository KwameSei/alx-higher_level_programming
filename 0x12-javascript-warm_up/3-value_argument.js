#!/usr/bin/node
/* Printing the 1st argument passed to it */
if (process.argv[2]) {
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
