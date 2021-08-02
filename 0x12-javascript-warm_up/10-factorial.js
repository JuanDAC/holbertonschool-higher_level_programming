#!/urs/bin/node

const { argv } = require('process');

const number = parseInt(Number(argv[2]));

const factorial = (number) => {
  if (number === 1) {
    return (1);
  }
  return (number * factorial(number - 1));
};

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
