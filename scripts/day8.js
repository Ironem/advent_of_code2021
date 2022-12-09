const fs = require("fs");

const checkOneStep = (grid, row, column, rowIndex, colIndex) => {
  if (grid[rowIndex][colIndex] < grid[row][column]) return true;
  return false;
};

const checkDirection = (grid, row, column, direction) => {
  let isVisible = true;
  switch (direction) {
    case "top":
      for (let index = row - 1; index >= 0; index--) {
        const visibility = checkOneStep(grid, row, column, index, column);
        if (!visibility) {
          isVisible = visibility;
          break;
        }
      }
      return isVisible;
    case "right":
      for (let index = column + 1; index < grid[row].length; index++) {
        const visibility = checkOneStep(grid, row, column, row, index);
        if (!visibility) {
          isVisible = visibility;
          break;
        }
      }
      return isVisible;
    case "botton":
      for (let index = row + 1; index < grid.length; index++) {
        const visibility = checkOneStep(grid, row, column, index, column);
        if (!visibility) {
          isVisible = visibility;
          break;
        }
      }
      return isVisible;
    case "left":
      for (let index = column - 1; index >= 0; index--) {
        const visibility = checkOneStep(grid, row, column, row, index);
        if (!visibility) {
          isVisible = visibility;
          break;
        }
      }
      return isVisible;
  }
};

const calculateDirectionScore = (grid, row, column) => {
  let allScore = 1;
  let localScore = 0;
  // TOP
  for (let index = row - 1; index >= 0; index--) {
    const visibility = checkOneStep(grid, row, column, index, column);
    if (!visibility) {
      localScore++;
      break;
    }
    localScore++;
  }
  allScore *= localScore;
  localScore = 0;
  // RIGHT
  for (let index = column + 1; index < grid[row].length; index++) {
    const visibility = checkOneStep(grid, row, column, row, index);
    if (!visibility) {
      localScore++;
      break;
    }
    localScore++;
  }
  allScore *= localScore;
  localScore = 0;
  // BOTTOM
  for (let index = row + 1; index < grid.length; index++) {
    const visibility = checkOneStep(grid, row, column, index, column);
    if (!visibility) {
      localScore++;
      break;
    }
    localScore++;
  }
  allScore *= localScore;
  localScore = 0;
  // LEFT
  for (let index = column - 1; index >= 0; index--) {
    const visibility = checkOneStep(grid, row, column, row, index);
    if (!visibility) {
      // localScore++;
      break;
    }
    localScore++;
  }
  allScore *= localScore;
  return allScore;
};

const updateVisibility = (grid, visibleTree) => {
  const newVisibleTree = visibleTree.map((row, rowIndex) => {
    if (rowIndex === visibleTree.length - 1 || rowIndex === 0) return row;
    return row.map((visibility, colIndex) => {
      if (visibility !== undefined) {
        return visibility;
      }
      // undefined case
      const localVisibility = [];
      // check TOP, RIGHT, BOTTOM, LEFT
      localVisibility.push(checkDirection(grid, rowIndex, colIndex, "top"));
      localVisibility.push(checkDirection(grid, rowIndex, colIndex, "right"));
      localVisibility.push(checkDirection(grid, rowIndex, colIndex, "botton"));
      localVisibility.push(checkDirection(grid, rowIndex, colIndex, "left"));
      if (localVisibility.includes(true)) return true;
      else return false;
    });
  });
  return newVisibleTree;
};

fs.readFile("./inputs/day8.txt", "utf8", (err, data) => {
  // fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");

  const grid = array.map((line) => line.split(""));
  const rows = grid.length;
  const cols = grid[0].length;
  let visibleTree = new Array(rows).fill().map((_, key) => {
    if (key === 0 || key === rows - 1) {
      return new Array(cols).fill().map(() => true);
    }
    return new Array(cols).fill().map((_, colInd) => {
      if (colInd === 0 || colInd === cols - 1) {
        return true;
      }
      return undefined;
    });
  });

  visibleTree = updateVisibility(grid, visibleTree);

  // part 1
  console.log(
    "Part 1: ",
    visibleTree.reduce(
      (acc, current) =>
        (acc += current.reduce(
          (acc2, current2) => (current2 ? (acc2 += 1) : acc2),
          0
        )),
      0
    )
  );

  const scenicScoreMap = grid.map((row, rowIndex) => {
    return row.map((val, colIndex) => {
      if (val === 0) return 0;
      if (
        colIndex === 0 ||
        colIndex === row.length - 1 ||
        rowIndex === 0 ||
        rowIndex === grid.length - 1
      )
        return 0;
      // check TOP, RIGHT, BOTTOM, LEFT score
      return calculateDirectionScore(grid, rowIndex, colIndex);
    });
  });

  // part 2
  console.log(
    "Part 2: ",
    Math.max(...scenicScoreMap.map((current) => Math.max(...current)))
  );
});
