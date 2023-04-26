#!/usr/bin/env node
/*
 * Stream response to a file stream
 */

const request = require('request');
const fs = require('fs');

request('http://localhost:5000/users').pipe(fs.createWriteStream('response.json'));
