# Initialising.
from pygame import *
init()

# Game window parameters.
width = 320
height = 480
mainWindow = display.set_mode((width, height))
display.set_caption("The Chronicles of Big Poppa")

# Images.
imageDictionary = {
    "frog": transform.scale(image.load("Images//Frog.png"), (30, 30)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (50, 50)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (80, 80)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (80, 80)),
    "background": transform.scale(image.load("Images//Background.png"), (320, 480))
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

frogX = centreImageXFrog(160, 30)
frogY = centreImageYFrog(240, 30)

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
                if frogY <= 30:
                    frogY += 0
                else:
                    frogY -= 30
                print("Frog Y:", frogY)
            if gameEvent.key == K_w:
                if frogY <= 30:
                    frogY += 0
                else:
                    frogY -= 30
                print("Frog Y:", frogY)
            if gameEvent.key == K_DOWN:
                if frogY >= 465:
                    frogY += 0
                else:
                    frogY += 30
                print("Frog Y:", frogY)
            if gameEvent.key == K_s:
                if frogY >= 465:
                    frogY += 0
                else:
                    frogY += 30
                print("Frog Y:", frogY)
            if gameEvent.key == K_LEFT:
                if frogX <= 35:
                    frogX += 0
                else:
                    frogX -= 30
                print("Frog X:", frogX)
            if gameEvent.key == K_a:
                if frogX <= 35:
                    frogX += 0
                else:
                    frogX -= 30
                print("Frog X:", frogX)
            if gameEvent.key == K_RIGHT:
                if frogX >= 295:
                    frogX += 0
                else:
                    frogX += 30
                print("Frog X:", frogX)
            if gameEvent.key == K_d:
                if frogX >= 295:
                    frogX += 0
                else:
                    frogX += 30
                print("Frog X:", frogX)
            # Background music control.
            if gameEvent.key == K_p:
                mixer.pause()
            if gameEvent.key == K_u:
                mixer.unpause()

    mainWindow.fill((0, 0, 0))
    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["background"], (0, 0))
    blitImage(imageDictionary["frog"], (centreImageXFrog(frogX, 30), (centreImageYFrog(frogY, 30))))
    # Renders the game.
    display.flip()