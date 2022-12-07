const fs = require("fs");

const TOTAL_SIZE = 70000000;
const UPDATE_SIZE = 30000000;

const updataOrCreateFolder = (pathToDir, fileSystem, data) => {
  let tmp = fileSystem;
  pathToDir.forEach((dir, key) => {
    if (key === pathToDir.length - 1) {
      if (tmp[dir]) {
        tmp[dir].files += data;
      } else {
        tmp[dir] = { files: 0 };
      }
    } else if (tmp[dir]) {
      tmp = tmp[dir];
    }
  });
};

const calculateDirTotal = (directory) => {
  let dirTotal = [0];
  Object.keys(directory).forEach((dirname) => {
    if (dirname === "files") {
      dirTotal[0] += parseInt(directory.files);
    } else {
      const subDirTotal = calculateDirTotal(directory[dirname]);
      dirTotal.push(...subDirTotal);
      dirTotal[0] += subDirTotal[0];
    }
  });
  return dirTotal;
};

fs.readFile("./inputs/day7.txt", "utf8", (err, data) => {
// fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const array = data.split("\r\n");

  const fileSystem = { "/": { files: 0 } };

  array.reduce((currentDir, line) => {
    const blocs = line.split(" ");
    if (blocs[0] === "$") {
      // command line
      if (blocs[1] === "cd") {
        if (blocs[2] === "..") {
          currentDir.pop();
        } else {
          currentDir.push(blocs[2]);
        }
      }
    } else if (blocs[0] === "dir") {
      let newDir = [...currentDir, blocs[1]];
      updataOrCreateFolder(newDir, fileSystem);
    } else {
      updataOrCreateFolder(currentDir, fileSystem, parseInt(blocs[0]));
    }
    return currentDir;
  }, []);

  const dirSize = calculateDirTotal(fileSystem["/"]);

  const needToFreeSize = UPDATE_SIZE - (TOTAL_SIZE - dirSize[0]);

  // if (needToFreeSize < 0) {
  //   console.log("enought");
  // } else {
  //   console.log("need free", needToFreeSize, dirSize);
  // }

  // part 1
  console.log(
    "Part 1: ",
    dirSize.reduce((acc, curr) => {
      if (curr <= 100000) {
        acc += curr;
      }
      return acc;
    }, 0)
  );
  // part 2
  console.log(
    "Part 2: ",
    dirSize.reduce((acc, curr) => {
      if (!acc) return curr;
      if (curr >= needToFreeSize && curr < acc) {
        acc = curr;
      }
      return acc;
    }, undefined)
  );
});
