#!/usr/bin/node
/* 
 * simple request example
 */

const request = require('request');

request('http://localhost:5000/users', function (error, response, body) {
	console.log('error:', error);
	console.log('body:', body);
	console.log('statusCode:', response && response.statusCode);
});
