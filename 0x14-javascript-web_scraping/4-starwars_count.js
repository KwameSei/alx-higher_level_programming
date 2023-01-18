#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body).results;
    let count = 0;
    for (const index in jsonBody) {
      const allCharacters = jsonBody[index].characters;
      for (const charIndex in allCharacters) {
        if (allCharacters[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
