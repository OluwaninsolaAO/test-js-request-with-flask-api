#!/usr/bin/env node
/*
 * explore request.get and request.post
 */

const request = require('request');

request
	.get('http://localhost:5000/users')
	.on('response', function (response) {
		console.log(response.statusCode);
		console.log(response.headers['content-type']);
	})
	.on('data', function (data) {
		console.log('body: ', data.toString());
	})
	.pipe(request.post('http://localhost:5000/users/repeat'))
	.on('response', function (response) {
		console.log(response.statusCode);
		console.log(response.headers['content-type']);
	})
	.on('data', function (data) {
		console.log('body: ', data.toString());
	});
