#!/usr/bin/node
const callMeMoby = function (num, func) {
  for (let i = 0; i < num; i++) {
    func();
  }
};
exports.callMeMoby = callMeMoby;
