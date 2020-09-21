#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      ocurrences++;
    }
  }
  return ocurrences;
};
