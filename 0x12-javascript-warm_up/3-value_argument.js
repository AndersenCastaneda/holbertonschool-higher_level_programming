#!/usr/bin/node
const argv = process.argv.slice(2);
for (const arg of argv) {
  if (arg != null) {
    console.log(arg);
  }
  break;
}
