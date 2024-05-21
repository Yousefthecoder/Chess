import pygame
import subprocess
import sys
import time

def round_to_nearest_100(value):
    return int((50 * round(value / 50) - 50) / 100)
action = True

click = []
adjusted_cordinate = []


game = True

list = ["K", "Q", "P", "B", "R", "KING"]
pygame.init()

# set display

width = 800
height = 800
run = True

# print board
white = (235, 236, 208)
green = (115, 149, 82)
LW = 100
colour = [white, green]

pygame.display.set_mode((width, height))
surface = pygame.display.set_mode((width, height))
placement = surface.subsurface(350, 730, 50, 70)
placement.set_colorkey()

i = 0
for x in range(0, 8 * LW, LW):
    for y in range(0, 8 * LW, LW):
        print(y)
        if ((x + y) / 100) % 2 == 0:
            i = 0
        else:
            i = 1
        pygame.draw.rect(surface, colour[i], pygame.Rect(x, y, LW, LW))

pygame.display.flip()
# images
# images
for x in range(len(list)):


    place_holder = "X:\My Drive\Chess\Chess\Chesspeice\W" + str(list[x]) + ".png"
    original_image = pygame.image.load(place_holder)


    if list[x] == "K":
        white_knight = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "Q":
        white_queen = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "B":
        white_bishop = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "KING":
        white_king = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "P":
        white_pawn = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "R":
        white_rook = pygame.transform.scale(original_image, (50, 70))

for x in range(len(list)):


    place_holder = "X:\My Drive\Chess\Chess\Chesspeice\B" + str(list[x]) + ".png"
    original_image = pygame.image.load(place_holder)


    if list[x] == "K":
        black_knight = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "Q":
        black_queen = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "B":
        black_bishop = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "KING":
        black_king = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "P":
        black_pawn = pygame.transform.scale(original_image, (50, 70))
    if list[x] == "R":
        black_rook = pygame.transform.scale(original_image, (50, 70))

# drawbox(x, y, width, length)
print("hey buddy")

# white
# 1 pawn
# 3 Knight
# 4 Bishop
# 5 Rook
# 8 Queen
# 9 King

cent_x = 25
cent_y = 20

board = [
    [15, 13, 14, 19, 18, 14, 13, 15],
    [11, 11, 11, 11, 11, 11, 11, 11],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [5, 3, 4, 9, 8, 4, 3, 5],
]


class chess_pieces:
    Color = ""

class King(chess_pieces):
    print("hey buddy")

class Queen(chess_pieces):
    print("hey buddy")
    pygame.display.set_caption("image")

    # create a surface object, image is drawn on it.
    # Using blit to copy content from one surface to other
    # paint screen one time
    pygame.display.flip()

class Knight(chess_pieces):
    print("hey buddy")

class Bishop(chess_pieces):
    print("hey buddy")

class Rook(chess_pieces):
    print("hey buddy")

class Pawn(chess_pieces):
    print("hey buddy")


for x in range(0, 8, 1):
    for y in range(0, 8, 1):
        if board[y][x] == 1:
            surface.blit(white_pawn, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 3:
            surface.blit(white_knight, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 4:
            surface.blit(white_bishop, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 5:
            surface.blit(white_rook, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 8:
            surface.blit(white_queen, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 9:
            surface.blit(white_king, ((x * LW) + cent_x, (y * LW) + cent_y))

        ##############################################################

        if board[y][x] == 11:
            surface.blit(black_pawn, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 13:
            surface.blit(black_knight, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 14:
            surface.blit(black_bishop, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 15:
            surface.blit(black_rook, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 18:
            surface.blit(black_queen, ((x * LW) + cent_x, (y * LW) + cent_y))

        if board[y][x] == 19:
            surface.blit(black_king, ((x * LW) + cent_x, (y * LW) + cent_y))
    pygame.display.update()

secondclick = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Record the click position
            pos = pygame.mouse.get_pos()
            click.append(pos)
            print(
                f"Click recorded at: {round_to_nearest_100(pos[0]), round_to_nearest_100(pos[1])}"
            )
            mx = round_to_nearest_100(pos[0])
            my = round_to_nearest_100(pos[1])
            print(board[my][mx])
            while secondclick == False:
                if board[my][mx] == 1:
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        time.sleep(0.01)
                        movement_positon = pygame.mouse.get_pos()
                        mx_2 = round_to_nearest_100(movement_positon[0])
                        my_2 = round_to_nearest_100(movement_positon[1])
                        print(my_2, my_2)
                        if board[my_2][mx_2] == 0 and my_2 == my + 1 or my + 2:
                            board[my][mx] = 0
                            board[my_2][mx_2] = 1
                            action = False
                            print(board[mx][my])
                            print(board[mx_2][my_2])
                            secondclick = True


while game == True:
    for x in range(0, 8, 1):
        for y in range(0, 8, 1):
            if board[y][x] == 1:
                surface.blit(white_pawn, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 3:
                surface.blit(white_knight, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 4:
                surface.blit(white_bishop, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 5:
                surface.blit(white_rook, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 8:
                surface.blit(white_queen, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 9:
                surface.blit(white_king, ((x * LW) + cent_x, (y * LW) + cent_y))

            ##############################################################


            if board[y][x] == 11:
                surface.blit(black_pawn, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 13:
                surface.blit(black_knight, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 14:
                surface.blit(black_bishop, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 15:
                surface.blit(black_rook, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 18:
                surface.blit(black_queen, ((x * LW) + cent_x, (y * LW) + cent_y))

            if board[y][x] == 19:
                surface.blit(black_king, ((x * LW) + cent_x, (y * LW) + cent_y))
    pygame.display.update()





