#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
let i;
if (isNaN(x)) {
  console.log('Missing size');
}
for (i = 0; i < x; i++) {
  console.log('X'.repeat(x));
}
