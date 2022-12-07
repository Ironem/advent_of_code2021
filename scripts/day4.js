const fs = require("fs");

const checkContains = (elf1, elf2) => {
  const [min1, max1] = elf1.split("-");
  const [min2, max2] = elf2.split("-");
  // left part contains right or right part contains left
  if (
    (parseInt(min1) <= parseInt(min2) && parseInt(max1) >= parseInt(max2)) ||
    (parseInt(min2) <= parseInt(min1) && parseInt(max2) >= parseInt(max1))
  )
    return true;
  return false;
};

const isOverlap = (elf1, elf2) => {
  const [min1, max1] = elf1.split("-");
  const [min2, max2] = elf2.split("-");
  // if left part is lower than the right part then check if max1 is greater than min2
  // if right part is lower than the left part then check if max2 is greater than min1
  if (
    (parseInt(min1) <= parseInt(min2) && parseInt(max1) >= parseInt(min2)) ||
    (parseInt(min1) >= parseInt(min2) && parseInt(max2) >= parseInt(min1))
  )
    return true;
  return false;
};

fs.readFile("./inputs/day4.txt", "utf8", (err, data) => {
  // fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");
  let res1 = 0;
  let res2 = 0;
  array.forEach((pair) => {
    const [firstElf, secondElf] = pair.split(",");
    if (checkContains(firstElf, secondElf)) res1++;
    if (isOverlap(firstElf, secondElf)) res2++;
  });

  // part 1
  console.log("Part 1: ", res1);
  // part 2
  console.log("Part 2: ", res2);
});
