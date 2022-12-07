const fs = require("fs");

const PART_1_LENGTH = 4;
const PART_2_LENGTH = 14;

const isMarker = (string, length) => {
  if (new Set(string.split("")).size === length) return true;
  return false;
};

fs.readFile("./inputs/day6.txt", "utf8", (err, data) => {
  // fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.replace(/\\r\\n/, "");

  let start = 0,
    part1End = 4,
    part2End = 14;
  while (
    part1End < array.length &&
    !isMarker(array.substring(start, part1End), PART_1_LENGTH)
  ) {
    part1End++;
    start++;
  }
  start = 0;
  while (
    part2End < array.length &&
    !isMarker(array.substring(start, part2End), PART_2_LENGTH)
  ) {
    part2End++;
    start++;
  }

  // part 1
  console.log("Part 1: ", part1End);
  // part 2
  console.log("Part 2: ", part2End);
});
