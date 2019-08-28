
import pygame
import random

from shape import *

newO = O({"x": 0, "y": 0}, 1, (255, 0, 0))
# def drawRect(window, x, y, w, h):
#     pygame.draw.rect(window, (255, 0, 0), (x, y, w, h))


# colors = {blue: (119, 115, 240), yellow: (236, 240, 115), red: (240, 115, 115), green: (
#     115, 240, 142), teal: (115, 240, 238), purple: (207, 115, 240)}


# draws 2d matrix on the game window
# the y index and the offset["y"] corresponds to the y position on the main game grid
# blocksize is the size of the individual block of the shape, should be square
def drawMatrix(window, matrix, offset, blockSize):
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] is not 0:
                pygame.draw.rect(
                    window, (255, 0, 0), (offset["x"] * blockSize + x * blockSize, offset["y"] * blockSize + y * blockSize, blockSize, blockSize), 1)


# creates a 2d array
def createMatrix(w, h):
    matrix = []
    for y in range(0, h):
        matrix.append([])
        for x in range(0, w):
            matrix[y].append(0)
    return matrix


def createArray(w):
    array = []
    for i in range(0, w):
        array.append(0)
    return array


arena = createMatrix(12, 20)


# debugging function


def printMatrixFormated(matrix):
    for row in matrix:
        print(row)
    print("end of matrix")


# placeholder matrix
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

# this function detects collision with other shapes and game window edges


def detectFullLine(matrix):
    indices = []
    for y in range(0, len(matrix)):
        rowIsFull = True
        for x in range(0, len(matrix[y])):
            if matrix[y][x] != 1:
                rowIsFull = False
                break
        if rowIsFull:
            indices.append(y)
    return indices


def collide(arena, player):
    m = player["matrix"]
    p = player["position"]

    # m = 3x3 matrix with the shape
    # p = shape cords offset("x","y")
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x] != 0:
                if y + p["y"] > len(arena)-1 or arena[y+p["y"]][x+p["x"]]:
                    return True
            else:
                continue
    return False


# this function puts the array of the shape into the main game array
# later used to render already dropped shapes and to detect colision with other shapes
def merge(arena, player):

    m = player["matrix"]
    p = player["position"]

    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            value = matrix[y][x]
            if value != 0:
                arenaRow = arena[y + p["y"]]
                arenaRow[x + p["x"]] = value


score = 0

# main function, entry point


def main():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans ', 30)

    # Program variables
    windowSize = (480, 900)
    window = pygame.display.set_mode(windowSize)
    pygame.display.set_caption("Tetris")
    wantsToPlay = True
    blockSize = 40
    timeDelay = 100

    fallSpeed = 50

    # img = pygame.image.load('./img/bg.png')

    # Placeholder position
    player = {"position": {"x": 0, "y": 0}, "matrix": matrix}

    fallTime = 0

    def handleFullLine(matrix):
        global score
        indices = detectFullLine(matrix)
        if indices != []:
            for index in indices:
                matrix.pop(index)
                matrix.insert(0, createArray(len(matrix[0])))
                score += 100

    # this function is used to drop the shape, used both manually(keyboard input) and based on time in the main loop of the game

    def dropShape():
        player["position"]["y"] += 1 #we need to check if the matrix is outside of arena to the right
        if(collide(arena, player)):
            player["position"]["y"] -= 1
            merge(arena, player)

            player["position"]["y"] = 0
            handleFullLine(arena)
            print(score)

    # this is the main drawing function of the program

    def draw():
        # get roation from shape instance function getRoation
        drawMatrix(window, player["matrix"], player["position"], blockSize)
        drawMatrix(window, arena, {"x": 0, "y": 0}, blockSize)

        # refreshes window
        pygame.display.update()
        # fills window so that the shapes do not get stay on the screen
        window.fill((0, 0, 0))

        pygame.draw.rect(window, (219, 187, 59), (0, 805, 480, 100), 10)
    while wantsToPlay:
        textsurface = myfont.render('Score: '+str(score), False, (255, 204, 0))
        fallTime += fallSpeed

        # Drops the shape
        if fallTime >= timeDelay:
            fallTime = 0
            dropShape()
        # Keyboard handler,  may want to change this to allow for continous drop when DOWN is pushed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # Temporary way of quitting the game(use "q" in the game window), change later to quit event
                    wantsToPlay = False
                elif event.key == pygame.K_LEFT:
                    # Move shape left
                    if(player["position"]["x"] >=1):
                        player["position"]["x"] -= 1
                elif(event.key == pygame.K_RIGHT):
                    # Move shape right
                    if(player["position"]["x"] <=8):
                        player["position"]["x"] += 1
                elif(event.key == pygame.K_UP):
                    # Rotate shape
                    pass
                elif(event.key == pygame.K_DOWN):
                    # Drop shape
                    dropShape()
                    fallTime = 0
       
        window.blit(textsurface, (150, 850))
        draw()

        # Delay so thay loop does not fire to quickly and to control the drop rate of the shape
        pygame.time.delay(timeDelay)

    pygame.quit()


if __name__ == '__main__':
    main()
