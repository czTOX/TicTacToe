import pygame
import math


def stav(pole):
    vysl = [
        [pole[0][0], pole[1][0], pole[2][0]], 
        [pole[0][1], pole[1][1], pole[2][1]],
        [pole[0][2], pole[1][2], pole[2][2]],
        [pole[0][0], pole[0][1], pole[0][2]],
        [pole[1][0], pole[1][1], pole[1][2]],
        [pole[2][0], pole[2][1], pole[2][2]],
        [pole[0][0], pole[1][1], pole[2][2]],
        [pole[2][0], pole[1][1], pole[0][2]],
    ]
    # X win  --> -1
    # Nic    --> 2
    # Remiza --> 0
    # O win  --> 1
    for item in vysl:
        if (item[0] != '') and (item[0] == item[1] == item[2]):
            if item[0] == 'o':
                return 1
            elif item[0] == 'x':
                return -1
    for col in pole:
        for item in col:
            if not item:
                return 2
    return 0


def minimax(pole, who, hloubka):
    var = stav(pole)
    if var != 2:
        return var
    if who:
        value = 5
        for x in range(3):
            for y in range(3):
                if not pole[x][y]:
                    pole[x][y] = 'x'
                    hodnota = minimax(pole, False, hloubka+1)
                    pole[x][y] = ''
                    value = min(value, hodnota)
    else:
        value = -5
        for x in range(3):
            for y in range(3):
                if not pole[x][y]:
                    pole[x][y] = 'o'
                    hodnota = minimax(pole, True, hloubka+1)
                    pole[x][y] = ''
                    value = max(value, hodnota)
    return value


run = True
koleckoNaTahu = True
pole = [['' for x in range(3)] for y in range(3)]
kolecko = pygame.image.load("D:/Python projekty/TicTacToe_v2/obrazky/kolecko.png")
krizek = pygame.image.load("D:/Python projekty/TicTacToe_v2/obrazky/krizek.png")


okno = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe")
okno.fill([212, 241, 249])
pygame.draw.line(okno, [0, 0, 0], (100, 0), (100, 300), 3)
pygame.draw.line(okno, [0, 0, 0], (200, 0), (200, 300), 3)
pygame.draw.line(okno, [0, 0, 0], (0, 100), (300, 100), 3)
pygame.draw.line(okno, [0, 0, 0], (0, 200), (300, 200), 3)
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = math.floor(x / 100)
            y = math.floor(y / 100)

            if koleckoNaTahu:
                if not pole[x][y]:
                    pole[x][y] = 'o'
                    okno.blit(kolecko, [x*100, y*100])
                    koleckoNaTahu = not koleckoNaTahu
                    pygame.display.update()
        now = stav(pole)
        if now != 2:
            if now == -1:
                print("X win")
            elif now == 1:
                print("O win")
            elif now == 0:
                print("Tie")
            run = False
        if not koleckoNaTahu:
            value = 5
            for x in range(3):
                for y in range(3):
                    if not pole[x][y]:
                        pole[x][y] = 'x'
                        hodnota = minimax(pole, False, 0)
                        pole[x][y] = ''
                        if hodnota < value:
                            value = hodnota
                            kde = [x, y]
            x = kde[0]
            y = kde[1]
            pole[x][y] = 'x'
    
            okno.blit(krizek, [x*100, y*100])
            koleckoNaTahu = not koleckoNaTahu
            pygame.display.update()
