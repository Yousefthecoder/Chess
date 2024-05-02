import pygame

game = True


pygame.init()


# set display

width = 800
height = 800
run = True

pygame.display.set_mode((width, height))
surface = pygame.display.set_mode((width, height))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # print board
    white = (255, 255, 255)
    green = (0, 255, 0)
    LW = 100
    colour = [white, green]

    # (x + y) % 2 if 0 then white esle green

    i = 0
    for x in range(0, 8 * LW, LW):
        for y in range(0, 8 * LW, LW):
            pygame.draw.rect(surface, colour[i], pygame.Rect(x, y, LW, LW))
            if i == 0:
                i = 1
            else:
                i = 0
    pygame.display.flip()

    # drawbox(x, y, width, length)

    print("hey buddy")

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

    board = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]
    while game == True:
        pygame.display.update()
