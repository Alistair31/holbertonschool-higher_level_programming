#!/usr/bin/node
const args = process.argv;
let x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (x > 0) {
  console.log('C is fun');
  x--;
}
