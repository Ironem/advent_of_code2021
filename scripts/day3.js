const fs = require("fs");

const calcultatePriority = (string) => {
  if (string === string.toLowerCase()) {
    return string.charCodeAt() - "a".charCodeAt() + 1;
  } else {
    return string.charCodeAt() - "A".charCodeAt() + 27;
  }
};

fs.readFile("./inputs/day3.txt", "utf8", (err, data) => {
  // fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");

  const duplicateString = [];
  const teamBadge = [];

  array.forEach((line) => {
    const tmp = [];
    const leftPart = line.split("").slice(0, line.length / 2);
    const rightPart = line.split("").slice(line.length / 2, line.length);
    leftPart.forEach((string) => {
      if (rightPart.includes(string) && !tmp.includes(string)) {
        tmp.push(string);
        duplicateString.push(string);
      }
    });
  });

  for (var i = 0; i < array.length; i += 3) {
    const elf1 = new Array(...new Set(array[i].split("")));
    const elf2 = array[i + 1].split("");
    const elf3 = array[i + 2].split("");
    elf1.forEach((string) => {
      if (elf2.includes(string) && elf3.includes(string)) {
        teamBadge.push(string);
      }
    });
  }
  const resultPart1 = duplicateString.reduce((state, current) => {
    state += calcultatePriority(current);
    return state;
  }, 0);
  const resultPart2 = teamBadge.reduce((state, current) => {
    state += calcultatePriority(current);
    return state;
  }, 0);

  // part 1
  console.log("Part 1: ", resultPart1);
  // part 2
  console.log("Part 2: ", resultPart2);
});
