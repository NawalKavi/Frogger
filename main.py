# Initialising.
from pygame import *
init()

# Game window parameters.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))
display.set_caption("The Chronicles of Big Poppa")

# Images.
imageDictionary = {
    "frog": transform.scale(image.load("Images//Frog.png"), (50, 50)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (70, 70)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (100, 100)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (100, 100))
}

# Audio.
audioDictionary = {
    "widePutin": mixer.Sound("Audio//Song For Denise (Perfect Loop).mp3"),
    "breakingBad": mixer.Sound("Audio//Breaking Bad (Extended Theme).mp3")
}

# Music whatnot.
mixer.Sound.play(audioDictionary["widePutin"])

# Finds the top-left corner coordinates of an image.
def centreImageX(xTarget, xSize):
    return xTarget - xSize / 2

def centreImageY(yTarget, ySize):
    return yTarget - ySize / 2

def centreImageXFrog(xTargetFrog, xSizeFrog):
    frogX = xTargetFrog - xSizeFrog / 2
    return frogX

def centreImageYFrog(yTargetFrog, ySizeFrog):
    frogY = yTargetFrog - ySizeFrog / 2
    return frogY

# Blitting or something.
def blitImage(imageAddress, xyValues):
    mainWindow.blit(imageAddress, xyValues)

frogX = centreImageXFrog(600, 40)
frogY = centreImageYFrog(600, 40)
frogChangeX = 0
frogChangeY = 0

# Game loop.
gameRunning = True
while gameRunning:
    for gameEvent in event.get():
        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False
        # Handles player movements.
        if gameEvent.type == KEYDOWN:
            if gameEvent.key == K_UP:
                if frogY <= -25:
                    frogChangeY += 0
                else:
                    frogChangeY -= 25
            if gameEvent.key == K_DOWN:
                if frogY <= -675:
                    frogChangeY += 0
                else:
                    frogChangeY += 25
            if gameEvent.key == K_LEFT:
                if frogX <= 25:
                    frogChangeX += 0
                else:
                    frogChangeX -= 25
            if gameEvent.key == K_RIGHT:
                if frogX >= 1175:
                    frogChangeX += 0
                else:
                    frogChangeX += 25
            # Background music control.
            if gameEvent.key == K_p:
                mixer.pause()
            if gameEvent.key == K_u:
                mixer.unpause()

    mainWindow.fill((0, 0, 0))
    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["frog"], ((centreImageXFrog(600, 40) + frogChangeX), (centreImageYFrog(600, 40) + frogChangeY)))
    # Renders the game.
    display.flip()