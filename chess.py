print("hey buddy")
LW=80
Color =1
# 1 pawn
# 3 Knight
# 4 Bishop
# 5 Rook
# 8 Queen
# 9 King

row_1 = [5, 3, 4, 9, 8, 4, 3, 5]
row_2 = [1, 1, 1, 1, 1, 1, 1, 1]
row_3 = [0, 0, 0, 0, 0, 0, 0, 0]
row_4 = [0, 0, 0, 0, 0, 0, 0, 0]
row_5 = [0, 0, 0, 0, 0, 0, 0, 0]
row_6 = [0, 0, 0, 0, 0, 0, 0, 0]
row_7 = [1, 1, 1, 1, 1, 1, 1, 1]
row_8 = [5, 3, 4, 9, 8, 4, 3, 5]

board = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]


print(board[7][0])

for x in range(0,7*LW,LW):
    for y in range(0,7*LW,LW):
     if Color > 0:
          print("hey buddy")

     if Color < 10:
          print("hey buddy")

         
     Color = Color*-1

class chess_pieces:
     Color = ""


class King(chess_pieces):
    print("hey buddy")


class Queen(chess_pieces):
    print("hey buddy")

class Knight(chess_pieces):
    print("hey buddy")


class Bishop(chess_pieces):
    print("hey buddy")


class Rook(chess_pieces):
    print("hey buddy")


class Pawn(chess_pieces):
    print("hey buddy")
