#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

Object.setPrototypeOf(myObject, {
  incr: function () {
    this.value += 1;
  }
});

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
