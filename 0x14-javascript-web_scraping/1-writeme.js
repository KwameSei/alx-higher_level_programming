#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const input = process.argv[3];

fs.writeFile(file, input, 'utf-8', function (err, input) {
  if (err) {
    console.log(err);
  }
});
