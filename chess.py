
import pygame
import subprocess


game = True


list = ["K", "Q", "P", "B", "R", "KING"]
pygame.init()




# set display


width = 800
height = 800
run = True


# images




pygame.display.set_mode((width, height))
surface = pygame.display.set_mode((width, height))
placement = surface.subsurface(350, 730, 50, 70)
placement.set_colorkey()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # print board
    white = (235, 236, 208)
    green = (115, 149, 82)
    LW = 100
    colour = [white, green]


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
        orginonal_image = pygame.image.load(place_holder).convert()


        if list[x] == "K":
            white_knight = pygame.transform.scale(orginonal_image, (50, 70))
        if list[x] == "Q":
            white_queen = pygame.transform.scale(orginonal_image, (50, 70))
        if list[x] == "B":
            white_bishop = pygame.transform.scale(orginonal_image, (50, 70))
        if list[x] == "KING":
            white_king = pygame.transform.scale(orginonal_image, (50, 70))
        if list[x] == "P":
            white_pawn = pygame.transform.scale(orginonal_image, (50, 70))
        if list[x] == "R":
            white_rook = pygame.transform.scale(orginonal_image, (50, 70))


    # drawbox(x, y, width, length)


    print("hey buddy")


    # 1 pawn
    # 3 Knight
    # 4 Bishop
    # 5 Rook
    # 8 Queen
    # 9 King


    board =[[5, 3, 4, 9, 8, 4, 3, 5],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [5, 3, 4, 9, 8, 4, 3, 5]]

    for x in range(0, 7, 1):
        for y in range(0, 7, 1):
            if board[x][y] == 1:
                surface.blit(white_pawn, (x * LW, y * LW))
                
            if board[x][y] == 3:
                surface.blit(white_knight, (x * LW, y * LW))
                
            if board[x][y] == 4:
                surface.blit(white_bishop, (x * LW, y * LW))
                
            if board[x][y] == 5:
                surface.blit(white_rook, (x * LW, y * LW))
                
            if board[x][y] == 8:
                surface.blit(white_queen, (x * LW, y * LW))
                
            if board[x][y] == 9:
                surface.blit(white_king, (x * LW, y * LW))
        

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



    while game == True:
        pygame.display.update()

