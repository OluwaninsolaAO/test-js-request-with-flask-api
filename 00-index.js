#!/usr/bin/node
/* 
 * simple request example
 */

const request = require('request');

request('http://localhost:5000/users', function (error, response, body) {
	console.log('error:', error);
	console.log('\nbody:', body);
	console.log('\nbody as json:', JSON.parse(body));
	console.log('\nstatusCode: ', response && response.statusCode);
});
