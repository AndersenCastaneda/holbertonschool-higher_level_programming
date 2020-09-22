#!/usr/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
const userTasksCompleted = {};

if (url) {
  request(url, function taskCompleted (err, response, body) {
    if (!err) {
      const json = JSON.parse(body);
      for (const task of json) {
        if (!(task.userId in userTasksCompleted)) {
          userTasksCompleted[task.userId] = 0;
        }
        if (task.completed === true) {
          ++userTasksCompleted[task.userId];
        }
      }
      console.log(userTasksCompleted);
    }
  });
}
