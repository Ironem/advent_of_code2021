const fs = require("fs");

const isAround = (prevNodePosition, curNodePosition) => {
  return (
    Math.abs(prevNodePosition[0] - curNodePosition[0]) <= 1 &&
    Math.abs(prevNodePosition[1] - curNodePosition[1]) <= 1
  );
};

const calculateNewPosition = (prevNodePosition, curNodePosition) => {
  const newPosition = [];
  if (prevNodePosition[0] > curNodePosition[0]) {
    newPosition.push(curNodePosition[0] + 1);
  } else if (prevNodePosition[0] === curNodePosition[0]) {
    newPosition.push(curNodePosition[0]);
  } else {
    newPosition.push(curNodePosition[0] - 1);
  }
  if (prevNodePosition[1] > curNodePosition[1]) {
    newPosition.push(curNodePosition[1] + 1);
  } else if (prevNodePosition[1] === curNodePosition[1]) {
    newPosition.push(curNodePosition[1]);
  } else {
    newPosition.push(curNodePosition[1] - 1);
  }
  return newPosition;
};

const moveOneStep = (ropePosition, vx, vy, visitedPosition) => {
  ropePosition.map((position, key) => {
    if (key !== 0) {
      if (!isAround(ropePosition[key - 1], position)) {
        const tmpPosition = calculateNewPosition(
          ropePosition[key - 1],
          position
        );
        position[0] = tmpPosition[0];
        position[1] = tmpPosition[1];
        if (key === ropePosition.length - 1)
          visitedPosition.add(`${position[0]}|${position[1]}`);
      }
    } else {
      if (vx !== 0) position[0] += vx;
      if (vy !== 0) position[1] += vy;
    }
    return position;
  });
};

const move = (ropePosition, direction, step, visitedPosition) => {
  for (let index = 0; index < step; index++) {
    switch (direction) {
      case "R":
        moveOneStep(ropePosition, 0, 1, visitedPosition);
        break;
      case "L":
        moveOneStep(ropePosition, 0, -1, visitedPosition);
        break;
      case "U":
        moveOneStep(ropePosition, 1, 0, visitedPosition);
        break;
      case "D":
        moveOneStep(ropePosition, -1, 0, visitedPosition);
        break;
    }
  }
};

fs.readFile("./inputs/day9.txt", "utf8", (err, data) => {
// fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");

  const ropePosition = [...new Array(2).fill().map(() => [0, 0])];
  const visitedPosition = new Set();
  visitedPosition.add("0|0");

  const ropePositionPart2 = [...new Array(10).fill().map(() => [0, 0])];
  const visitedPositionPart2 = new Set();
  visitedPositionPart2.add("0|0");

  array.forEach((moveOrder) => {
    const [direction, step] = moveOrder.split(" ");
    move(ropePosition, direction, parseInt(step), visitedPosition);
    move(ropePositionPart2, direction, parseInt(step), visitedPositionPart2);
  });

  // part 1
  console.log("Part 1: ", visitedPosition.size);

  // part 2
  console.log("Part 2: ", visitedPositionPart2.size);
});
