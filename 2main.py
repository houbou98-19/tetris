
import pygame
import random

from shape import *

x = O([3, 4], 1, (255, 0, 0))
# def drawRect(window, x, y, w, h):
#     pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))


# colors = {blue: (119, 115, 240), yellow: (236, 240, 115), red: (240, 115, 115), green: (
#     115, 240, 142), teal: (115, 240, 238), purple: (207, 115, 240)}


def drawMatrix(window, matrix, offset, blockSize):
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] is not 0:
                pygame.draw.rect(
                    window, (255, 0, 0), (offset["x"] * blockSize + x * blockSize, offset["y"] * blockSize + y * blockSize, blockSize, blockSize))


def createMatrix(w, h):
    matrix = []

    for y in range(0, h):
        matrix.append([])
        for x in range(0, w):
            matrix[y].append(0)
    print(len(matrix))
    return matrix


arena = createMatrix(10, 20)

matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]


def collide(arena, player):
    m = player["matrix"]
    p = player["position"]

    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x] != 0:
                if y + p["y"] > len(arena)-1:
                    return True
                else:
                    break
    return False


def merge(arena, player):

    m = player["matrix"]
    p = player["position"]

    print(player)
    for x in range(0, len(m)):
        for y in range(0, len(m[x])):
            value = matrix[x][y]
            if value != 0:

                arena[y + p["y"]][x + p["x"]] = value


def main():

    def dropShape():
        player["position"]["y"] = player["position"]["y"]+1
        if(collide(arena, player)):
            player["position"]["y"] -= 1
            merge(arena, player)
            # for row in arena:
            #     print(row)
            # print("")

            player["position"]["y"] = 0
        print(player)

    def draw():
        drawMatrix(window, player["matrix"], player["position"], blockSize)
        drawMatrix(window, arena, {"x": 0, "y": 0}, blockSize)
        pygame.display.update()
        window.fill((0, 0, 0))
    pygame.init()

    windowSize = (480, 800)
    window = pygame.display.set_mode(windowSize)
    pygame.display.set_caption("Tetris")
    wantsToPlay = True
    blockSize = 40
    timeDelay = 100

    fallSpeed = 10

    player = {"position": {"x": 0, "y": 0}, "matrix": matrix}

    fallTime = 0
    while wantsToPlay:
        fallTime += fallSpeed

        if fallTime >= timeDelay:
            fallTime = 0
            dropShape()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    wantsToPlay = False

                elif event.key == pygame.K_LEFT:
                    player["position"]["x"] = player["position"]["x"] - 1
                elif(event.key == pygame.K_RIGHT):
                    player["position"]["x"] = player["position"]["x"] + 1
                elif(event.key == pygame.K_UP):
                    pass
                elif(event.key == pygame.K_DOWN):
                    dropShape()
                    fallTime = 0

        draw()
        pygame.time.delay(timeDelay)

    pygame.quit()


if __name__ == '__main__':
    main()
