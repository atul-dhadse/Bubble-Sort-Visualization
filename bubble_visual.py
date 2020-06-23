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
TOTALBARS = 150
LINEHEIGHT = 98
BARWIDTH = 5

LINECOLOR = WHITE
TIMERFONTSIZE = 150

#gap between two bars
GAP = 3

#gap between bar's height
STEP = 5

FPS = 120

#actual gap
ACTUALGAP = BARWIDTH + GAP

# x-coordinate of the first bar
XSTART = (WINDOWWIDTH - (TOTALBARS*(ACTUALGAP)))//2 

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

    drawBars(numList,BARCOLOR, 60)

    timerMsg(3, 100, 100, BARCOLOR, TIMERFONTSIZE)

    XMARGIN = XSTART    

    for i in range(len(numList)):
        for j in range(len(numList) - 1):
            checkForQuit()
            drawMsg("Press Esc to exit..", 20, 20, WHITE, 30)
            if numList[j] > numList[j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
                x, y = XMARGIN, WINDOWHEIGHT - LINEHEIGHT - MAX - 4
                pygame.draw.rect(DISPLAYSURF, BGCOLOR, (x, y, 2 * ACTUALGAP, MAX))
                x1, y1 = XMARGIN, WINDOWHEIGHT - LINEHEIGHT - numList[j]
                x2, y2 = XMARGIN + ACTUALGAP, WINDOWHEIGHT - LINEHEIGHT - numList[j + 1]
                pygame.draw.rect(DISPLAYSURF, getRandomColor(), (x1,y1, BARWIDTH, numList[j]))
                pygame.draw.rect(DISPLAYSURF, getRandomColor(), (x2,y2, BARWIDTH, numList[j + 1]))
                XMARGIN += ACTUALGAP
            else:
                XMARGIN += ACTUALGAP
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            # drawBars(numList,WHITE,None)
        numList = numList[:len(numList)-1]
        XMARGIN = XSTART

    timerMsg(3, 100, 100, GREEN, TIMERFONTSIZE)

    DISPLAYSURF.fill(BLACK)
    drawBars(sortedList, WHITE, None)
    drawBars(sortedList, GREEN, 30)
    pygame.display.flip()

    while True:
        drawMsg("Press Esc to exit..", 5, 5, GREEN, 30)
        checkForQuit()

def getRandomColor():
    return (random.randint(50,255),random.randint(50,255),random.randint(50,255))

def drawMsg(msg, x, y, color, fontSize):
    BASICFONT = pygame.font.Font("freesansbold.ttf", fontSize)
    msgSurf = BASICFONT.render(msg, True, color, BGCOLOR)
    msgRect = msgSurf.get_rect()
    msgRect.topleft = (x, y)
    DISPLAYSURF.blit(msgSurf, msgRect)

def drawBars(numList,color,fps = None):
    XMARGIN = XSTART
    for num in numList:
        drawMsg("Press Esc to exit..", 20, 20, WHITE, 30)
        checkForQuit()
        Y = WINDOWHEIGHT - LINEHEIGHT - num - 3
        pygame.draw.rect(DISPLAYSURF, color, (XMARGIN, Y, BARWIDTH, num))
        if fps != None:
            FPSCLOCK.tick(fps)
            pygame.display.flip()
        XMARGIN += ACTUALGAP
    pygame.display.flip()

def timerMsg(howMuchTime, x, y , color, fontSize):
    BASICFONT = pygame.font.Font("freesansbold.ttf", fontSize)
    for i in range(howMuchTime + 1):
        checkForQuit()
        msgSurf = BASICFONT.render(str(howMuchTime - i), True, color)
        msgRect = msgSurf.get_rect()
        msgRect.topleft = (x, y)
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (x, y, fontSize, fontSize))
        DISPLAYSURF.blit(msgSurf, msgRect)
        pygame.display.update()
        pygame.time.wait(1000)
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (x, y, fontSize, fontSize))

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
