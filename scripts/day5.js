const fs = require("fs");

const makeAmove = (move, stacksArray) => {
  const [nb, from, to] = move
    .replace(/[movefrt]/g, "")
    .trim()
    .split("  ");
  for (let index = 0; index < parseInt(nb); index++) {
    const moveElement = stacksArray[parseInt(from) - 1].pop();
    stacksArray[parseInt(to) - 1].push(moveElement);
  }
};

const makeAmovePart2 = (move, stacksArray) => {
  const [nb, from, to] = move
    .replace(/[movefrt]/g, "")
    .trim()
    .split("  ");
  const moveElement = stacksArray[parseInt(from) - 1].splice(
    stacksArray[parseInt(from) - 1].length - parseInt(nb),
    stacksArray[parseInt(from) - 1].length
  );
  stacksArray[parseInt(to) - 1].push(...moveElement);
};

fs.readFile("./inputs/day5.txt", "utf8", (err, data) => {
  // fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");

  const stacks = [];
  const moves = [];
  let stackOver = false;
  array.forEach((line) => {
    if (line === "") {
      stackOver = true;
    } else if (stackOver) {
      moves.push(line);
    } else {
      stacks.push(line);
    }
  });

  const nbStacks = stacks.pop().replace(/ /g, "").length;

  const stacksArray = [];
  const stacksArray2 = [];
  for (let index = 0; index < nbStacks; index++) {
    stacksArray.push([]);
    stacksArray2.push([]);
  }

  while (stacks.length > 0) {
    let stackLine = stacks.pop();
    if (stackLine[0] === " ") stackLine = stackLine.replace(/    /, "[] ");

    // replace all empty space by []
    stackLine
      .replace(/    /g, " []")
      .split(" ")
      .forEach((letter, key) => {
        if (letter.replace(/[\[\]]/g, "")) {
          stacksArray[key].push(letter.replace(/[\[\]]/g, ""));
          stacksArray2[key].push(letter.replace(/[\[\]]/g, ""));
        }
      });
  }

  moves.forEach((move) => {
    makeAmove(move, stacksArray);
    makeAmovePart2(move, stacksArray2);
  });

  // part 1
  console.log(
    "Part 1: ",
    stacksArray.reduce((acc, curr) => {
      acc += curr.pop();
      return acc;
    }, "")
  );
  // part 2
  console.log(
    "Part 2: ",
    stacksArray2.reduce((acc, curr) => {
      acc += curr.pop();
      return acc;
    }, "")
  );
});
