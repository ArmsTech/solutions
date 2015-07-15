var boardSize = 8;
var chessBoard = '';

for (var i = 0; i < boardSize; i++) {
  for (var j = 0; j < boardSize; j++) {
    if ((i + j) % 2 === 0)
      chessBoard += ' ';
    else
      chessBoard += '#';
  }
  chessBoard += '\n';
}

console.log(chessBoard);
