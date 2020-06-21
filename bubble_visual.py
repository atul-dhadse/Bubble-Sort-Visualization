import pygame
import random
import sys
from pygame.locals import *
import time

WINDOWWIDTH = 1500
WINDOWHEIGHT = 900

BLACK =  (0,0,0)
RED = (255,51,51)
GREEN = (0,255,0)
BLUE = (0,255,255)
WHITE = (255,255,255)
ORANGE = (255, 165, 0)

BGCOLOR = BLACK
BARCOLOR = ORANGE
TOTALBARS = 100
LINEHEIGHT = 98
BARWIDTH = 5
# XSTART = WINDOWWIDTH/2 - (TOTALBARS/2)*(BARWIDTH)
XSTART = (WINDOWWIDTH - (TOTALBARS)*(BARWIDTH + 2))/2
LINECOLOR = WHITE

#gap between bar's height
STEP = 5

FPS = 30

def main():
    global DISPLAYSURF, FPSCLOCK, XMARGIN
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK = pygame.time.Clock()
    XMARGIN = XSTART

    numList = list(range(STEP, (TOTALBARS + 1)*STEP, STEP))
    sortedList = numList.copy()
    MAX = numList[-1]
    random.shuffle(numList)

    DISPLAYSURF.fill(BGCOLOR)
    pygame.draw.line(DISPLAYSURF, LINECOLOR, (0, WINDOWHEIGHT - LINEHEIGHT), (WINDOWWIDTH, WINDOWHEIGHT - LINEHEIGHT),5)

    drawBars(numList,BARCOLOR)

    time.sleep(2)

    XMARGIN = XSTART    

    for i in range(len(numList)):
        for j in range(len(numList) - 1):
            checkForQuit()
            if numList[j] > numList[j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
                x, y = XMARGIN, WINDOWHEIGHT - LINEHEIGHT - MAX - 4
                pygame.draw.rect(DISPLAYSURF, BGCOLOR, (x,y,14, MAX))
                x1, y1 = XMARGIN, WINDOWHEIGHT - LINEHEIGHT - numList[j]
                x2, y2 = XMARGIN + 7, WINDOWHEIGHT - LINEHEIGHT - numList[j + 1]
                pygame.draw.rect(DISPLAYSURF, (random.randint(100,255),random.randint(100,255),random.randint(20,255)), (x1,y1, BARWIDTH, numList[j]))
                pygame.draw.rect(DISPLAYSURF, (random.randint(100,255),random.randint(100,255),random.randint(20,255)), (x2,y2, BARWIDTH, numList[j + 1]))
                XMARGIN += 7
            else:
                XMARGIN += 7
            pygame.display.update()
            FPSCLOCK.tick(FPS)
        numList = numList[:len(numList)-1]
        XMARGIN = XSTART

    pygame.time.wait(500)
    DISPLAYSURF.fill(BLACK)
    drawBars(sortedList, GREEN)
    pygame.display.flip()


    while True:
        checkForQuit()


def drawBars(numList,color):
    XMARGIN = XSTART
    for num in numList:
        checkForQuit()
        Y = WINDOWHEIGHT - LINEHEIGHT - num - 3
        pygame.draw.rect(DISPLAYSURF, color, (XMARGIN, Y, BARWIDTH, num))
        pygame.display.flip()
        FPSCLOCK.tick(60)
        XMARGIN += 7


def checkForQuit():
    for event in pygame.event.get(QUIT):
        sys.exit()
        pygame.quit()
    for event in pygame.event.get():
        if event.type == KEYUP and event.key == K_ESCAPE:
            sys.exit()
            pygame.quit()

if __name__ == "__main__":
    main()
