const fs = require("fs");

const winCondition = {
  Rock: "Scissors",
  Scissors: "Paper",
  Paper: "Rock",
};

const calculateMatchScore = (a, b) => {
  if (a === b) return 3;
  if (winCondition[b] === a) {
    return 6;
  }
  return 0;
};

const calculateSign = (opponentSign, result) => {
  if (result === 3) return opponentSign;
  if (result > 3) return winCondition[winCondition[opponentSign]]; 
  else {
    return winCondition[opponentSign];
  }
};

fs.readFile("./inputs/day2.txt", "utf8", (err, data) => {
// fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\n");

  const elfSign = { A: "Rock", B: "Paper", C: "Scissors" };
  const mySign = { X: "Rock", Y: "Paper", Z: "Scissors" };
  const myResult = { X: 0, Y: 3, Z: 6 };
  const signScore = { Rock: 1, Scissors: 3, Paper: 2 };

  const result = array.reduce(
    (state, current) => {
      const [elf, me] = current.split(" ");
      const realMe = me.trim();
      state[0] +=
        calculateMatchScore(elfSign[elf], mySign[realMe]) +
        signScore[mySign[realMe]];

      state[1] +=
        myResult[realMe] +
        signScore[calculateSign(elfSign[elf], myResult[realMe])];
      return state;
    },
    [0, 0]
  );

  // part 1
  console.log("Part 1: ", result[0]);
  // part 2
  console.log("Part 2: ", result[1]);
});
