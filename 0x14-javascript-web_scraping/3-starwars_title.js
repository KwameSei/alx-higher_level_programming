#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
