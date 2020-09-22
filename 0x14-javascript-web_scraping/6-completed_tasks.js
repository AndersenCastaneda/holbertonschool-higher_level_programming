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
        if (task.completed === true) {
          if (!(task.userId in userTasksCompleted)) {
            userTasksCompleted[task.userId] = 1;
          } else {
            userTasksCompleted[task.userId]++;
          }
        }
      }
      console.log(userTasksCompleted);
    }
  });
}
