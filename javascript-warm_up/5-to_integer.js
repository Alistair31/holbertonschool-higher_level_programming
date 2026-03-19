#!/usr/bin/node
const args = process.argv;
const n = parseInt(args[2]);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number:', n);
}
