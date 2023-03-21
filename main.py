# Initialising.
from pygame import *
from random import *
init()


# Game window parameters.
width = 320
height = 480
mainWindow = display.set_mode((width, height))
display.set_caption("The Chronicles of Big Poppa")


# Images.
imageDictionary = {
    "frog": transform.scale(image.load("Images//Frog.png"), (30, 30)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (35, 35)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (40, 40)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (40, 40)),
    "background": transform.scale(image.load("Images//Background.png"), (320, 480))
}


# Audio.
audioDictionary = {
    "breakingBad": mixer.Sound("Audio//Breaking Bad Theme Song (8 Bit).mp3"),
    "a-Ha": mixer.Sound("Audio//Take On Me (8 Bit).mp3"),
    "daftPunk": mixer.Sound("Audio//Harder Better Faster Stronger (8 Bit).mp3"),
    "rickRoll": mixer.Sound("Audio//Never Gonna Give You Up (8 Bit).mp3")
}


# Finds the top-left corner coordinates of an image.
def centreImageXFrog(xTargetFrog, xSizeFrog):
    frogX = xTargetFrog - xSizeFrog / 2
    return frogX

def centreImageYFrog(yTargetFrog, ySizeFrog):
    frogY = yTargetFrog - ySizeFrog / 2
    return frogY


# Blitting or something.
def blitImage(imageAddress, xyValues):
    mainWindow.blit(imageAddress, xyValues)

frogX = centreImageXFrog(175, 30)
frogY = centreImageYFrog(385, 30)


class Car():
    def __init__(self, targetX, targetY, carSizeX, carSizeY):
        self.targetX = targetX
        self.targetY = targetY
        self.carSizeX = carSizeX
        self.carSizeY = carSizeY

    def centreCarX(self):
        return self.targetX - self.carSizeX / 2

    def centreCarY(self):
        return self.targetY - self.carSizeY / 2

    def blitCar(self):
        mainWindow.blit(imageDictionary["redCar"], (self.centreCarX(), self.centreCarY()))

redCar = Car(30, 310, 50, 50)


# Music whatnot.
audioArray = ["breakingBad", "a-Ha", "daftPunk", "rickRoll"]
audioSelector = randint(0, 3)
mixer.Sound.play(audioDictionary[audioArray[audioSelector]])


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
                if frogY >= 460:
                    frogY += 0
                else:
                    frogY += 30
                print("Frog Y:", frogY)
            if gameEvent.key == K_s:
                if frogY >= 460:
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
    # Initial Background.
    mainWindow.fill((0, 0, 0))
    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["background"], (0, 0))
    # River.
    draw.rect(mainWindow, (7, 11, 120), Rect(00, 90, 320, 157))
    blitImage(imageDictionary["frog"], (centreImageXFrog(frogX, 30), (centreImageYFrog(frogY, 30))))
    redCar.blitCar()
    # Renders the game.
    display.flip()