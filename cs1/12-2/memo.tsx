type Position = [number, number];
const findSevenPositions = (arr: number[][]): Position[] => {
  const positions: Position[] = [];
  arr.map((row, i) => {
    row.map((value, j) => {
      if (value === 7) {
        positions.push([i, j]);
      }
    });
  });
  return positions;
};

const findIntermediatePositions = (arr: number[][]): Position[] => {
  const sevens = findSevenPositions(arr);
  const [x1, y1] = sevens[0];
  const [x2, y2] = sevens[1];
  const positions: Position[] = [];
  const xStep = x2 > x1 ? 1 : x2 < x1 ? -1 : 0;
  const yStep = y2 > y1 ? 1 : y2 < y1 ? -1 : 0;
  let x = x1 + xStep;
  let y = y1 + yStep;
  while (x !== x2 || y !== y2) {
    positions.push([x, y]);
    x += xStep;
    y += yStep;
  }
  return positions;
};
const board = [
  [7, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 7],
];
console.log(findIntermediatePositions(board)); // Returns the positions of the elements between the sevens
