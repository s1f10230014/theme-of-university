var findSevenPositions = function (arr) {
  var positions = [];
  arr.map(function (row, i) {
    row.map(function (value, j) {
      if (value === 7) {
        positions.push([i, j]);
      }
    });
  });
  return positions;
};
var findIntermediatePositions = function (arr) {
  var sevens = findSevenPositions(arr);
  var _a = sevens[0],
    x1 = _a[0],
    y1 = _a[1];
  var _b = sevens[1],
    x2 = _b[0],
    y2 = _b[1];
  var positions = [];
  var xStep = x2 > x1 ? 1 : x2 < x1 ? -1 : 0;
  var yStep = y2 > y1 ? 1 : y2 < y1 ? -1 : 0;
  var x = x1 + xStep;
  var y = y1 + yStep;
  while (x !== x2 || y !== y2) {
    positions.push([x, y]);
    x += xStep;
    y += yStep;
  }
  return positions;
};
var board = [
  [7, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 7],
];
console.log(findIntermediatePositions(board)); // Returns the positions of the elements between the sevens
