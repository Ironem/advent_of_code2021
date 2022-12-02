const fs = require("fs");

fs.readFile("./inputs/day1.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  let indice = 0;
  const array = data.split("\n");

  const result = array.reduce((state, current) => {
    const currentNumber = parseInt(current);
    if (isNaN(currentNumber)) {
      indice++;
    } else {
      state[indice]
        ? (state[indice] += currentNumber)
        : (state[indice] = currentNumber);
    }
    return state;
  }, []);
  result.sort((a, b) => {
    return b - a;
  });
  // part1
  console.log("Part 1: ", result[0]);
  // part1
  console.log("Part 2: ", result[0] + result[1] + result[2]);
});
