#!/usr/bin/env node
/*
 * Takes in a positional arguement of URL to the API to be tested
 * dumps the response as a JSON string to a file.
 */

const request = require("request");
const fs = require("fs");

if (process.argv.length !== 3) {
  return;
}

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log("Response Recieved:\n", data);
    fs.writeFile("response.json", body, function (error) {
      console.log(error);
      return;
    });
  }
});
