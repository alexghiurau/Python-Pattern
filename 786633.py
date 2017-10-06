# 786633.py
# Made by Alexandru Ghiurau - UP786633
# A Patchwork Sampler

from graphics import *

def main():
    x = 0 # coord constants
    y = 0
    patchSize, patchColoursList = getInputs()
    win = drawWindow(patchSize)
    drawPatchwork1(win, x, y, patchSize, patchColoursList)
    drawPatchwork2Color1(win, x, y, patchSize, patchColoursList)
    drawPatchwork2Single(win, x, y, patchSize, patchColoursList)
    drawPatchwork2Color3(win, x, y, patchSize, patchColoursList)
    drawRects(win, x, y, patchSize, patchColoursList)

def drawWindow(patchSize):
    win = GraphWin("Patchwork Sampler", patchSize*100, patchSize*100)
    return win

def getInputs():
    patchSize = eval(input("Enter the patch size: "))
    patchColoursList = []
    while True:
        colour = input("Enter colour (ret to exit): ")
        if colour == "":
            break
        patchColoursList.append(colour)
    while patchSize not in (5, 7, 9):
        print("Sorry, invalid number!")
        patchSize = eval(input("Enter the patch size: "))
    return patchSize, patchColoursList

def drawPatch1(win, x, y, colour):
    centre = Point(x + 10, y + 10)
    circles = Circle(centre, 10)
    circles.setOutline(colour)
    circles.draw(win)

def drawVertical(win, x, y, colour):
    rect = Rectangle(Point(x+10,y), Point(x+20, y+20))
    rect.setOutline(colour)
    rect.setFill(colour)
    rect.draw(win)

def drawHorizontal(win, x, y, colour):
    rectV = Rectangle(Point(x + 20, y), Point(x + 40, y + 10))
    rectV.setOutline(colour)
    rectV.setFill(colour)
    rectV.draw(win)

def drawRects(win, x, y, patchSize, patchColoursList):
    patch1Size = patchSize // 2
    patch2Size = patchSize // 2 + 1
    for y in range(0, patch1Size * 100, 20):
        for x in range(0, patch2Size * 100, 40):
            drawVertical(win, x, y, patchColoursList[0])
    for y in range(patch1Size * 100, patchSize * 100, 20):
        for x in range(patch2Size * 100, patchSize * 100, 40):
            drawVertical(win, x, y, patchColoursList[2])
    for y in range(0, patch1Size * 100, 20):
        for x in range(patch2Size * 100, patchSize * 100, 40):
            drawVertical(win, x, y, patchColoursList[1])
    for y in range(0, patch1Size * 100, 20):
        for x in range(0, patch2Size * 100, 40):
            drawHorizontal(win, x, y, patchColoursList[0])
    for y in range(patch1Size * 100, patchSize * 100, 20):
        for x in range(patch2Size * 100, patchSize * 100, 40):
            drawHorizontal(win, x, y, patchColoursList[2])
    for y in range(0, patch1Size * 100, 20):
        for x in range(patch2Size * 100, patchSize * 100, 40):
            drawHorizontal(win, x, y, patchColoursList[1])


def drawPatchwork1(win, x, y, patchSize, patchColoursList):
    patch1Size = patchSize // 2
    patch2Size = patchSize // 2 + 1
    for y in range(0, patch1Size * 100, 20):
        for x in range(0, patchSize * 100, 20):
            drawPatch1(win, x, y, patchColoursList[0])
    for y in range(patch1Size * 100, patchSize * 100, 20):
         for x in range(patch2Size * 100, patchSize * 100, 20):
             drawPatch1(win, x, y, patchColoursList[2])
    for y in range(0, patch1Size * 100, 20):
         for x in range(patch2Size * 100, patchSize * 100, 20):
             drawPatch1(win, x, y, patchColoursList[1])

def drawPatch2(win,x,y,colour):
    for i in range(10):
        lines1 = Line(Point(i*10 + x, 0 + y), Point((10-i)*10 + x, 100 + y))
        lines1.setOutline(colour)
        lines1.draw(win)
        lines2 = Line(Point(100 + x ,i*10 + y), Point(0 + x,(10 - i)*10 + y))
        lines2.setOutline(colour)
        lines2.draw(win)

def drawPatchwork2Color1(win, x, y, patchSize, patchColoursList):
    patch1Size = patchSize // 2
    patch2Size = patchSize // 2 + 1
    i = 0
    for y in range((patch1Size + i) * 100, (patchSize - 1) * 100, 100):
        for x in range(0, patch1Size * 100, 100):
            drawPatch2(win, x, y, patchColoursList[0])
            i = i + 1

def drawPatchwork2Single(win, x, y, patchSize, patchColoursList):
    patch1Size = patchSize // 2
    patch2Size = patchSize // 2 + 1
    y = y + (patch1Size * 100)
    for x in range(patch1Size * 100, -1, -100):
        drawPatch2(win, x, y, patchColoursList[1])
        y = y + 100

def drawPatchwork2Color3(win, x, y, patchSize, patchColoursList):
    patch1Size = patchSize // 2
    patch2Size = patchSize // 2 + 1
    y = y + ((patch1Size + 1) * 100)
    for x in range(patch1Size * 100, -1, -100):
        drawPatch2(win, x, y, patchColoursList[2])
        y = y + 100
    if patchSize == 5:
        x = patch1Size * 100
        y = (patchSize - 1) * 100
        drawPatch2(win, x, y, patchColoursList[2])
    elif patchSize == 7:
        for y in range(500, 700, 100):
            for x in range(200, 400, 100):
                drawPatch2(win, x, y, patchColoursList[2])
    elif patchSize == 9:
        for y in range(700, 900, 100):
            for x in range(200, 400, 100):
                drawPatch2(win, x, y, patchColoursList[2])
        for y in range(600, 900, 100):
            for x in range(400,500,100):
                drawPatch2(win, x, y, patchColoursList[2])
