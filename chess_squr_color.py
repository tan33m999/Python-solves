def getChessSquareColor(column, row):
    if column <= 7 and row <= 7 :
        if (column * row) % 2 == 0:
            return "black"
        elif (column * row) % 2 == 1:
            return "white"
    else:
        return ''

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == ''
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
