# Initialising.
from pygame import *
from random import *
init()
gameRunning = True

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
    "rickRoll": mixer.Sound("Audio//Never Gonna Give You Up (8 Bit).mp3"),
    "polishCow": mixer.Sound("Audio//Polish Cow (8 Bit).mp3"),
    "downUnder": mixer.Sound("Audio//Down Under (8 Bit).mp3")
}


# Blitting or something.
def blitImage(imageAddress, xyValues):
    mainWindow.blit(imageAddress, xyValues)

class Frog:
    def __init__(self, xTargetFrog, yTargetFrog, xSizeFrog, ySizeFrog, frogX, frogY):
        self.xTargetFrog = xTargetFrog
        self.yTargetFrog = yTargetFrog
        self.xSizeFrog = xSizeFrog
        self.ySizeFrog = ySizeFrog
        self.frogX = frogX
        self.frogY = frogY

    def centreFrogX(self):
        self.frogX = self.xTargetFrog - self.xSizeFrog / 2
        return self.frogX

    def centreFrogY(self):
        self.frogY = self.yTargetFrog - self.ySizeFrog / 2
        return self.frogY

    def upMove(self):
        if self.frogY >= 30:
            self.frogY -= 30
        print("Frog Y:", self.frogY)

    def downMove(self):
        if self.frogY <= 460:
            self.frogY += 30
        print("Frog Y:", self.frogY)

    def leftMove(self):
        if self.frogX >= 35:
            self.frogX -= 30
        print("Frog X:", self.frogX)

    def rightMove(self):
        if self.frogX <= 295:
            self.frogX += 0

        print("Frog X:", self.frogX)

    def drowningDetection(self):
        if self.frogY:
            pass

    def blitImage(self):
        mainWindow.blit(imageDictionary["frog"], (self.centreFrogX(), self.centreFrogY()))

bigPoppa = Frog(160, 385, 30, 30, None, None)

class Car:
    def __init__(self, targetX, targetY, carSizeX, carSizeY):
        self.targetX = targetX
        self.targetY = targetY
        self.carSizeX = carSizeX
        self.carSizeY = carSizeY

    def centreCarX(self):
        carX = self.targetX - self.carSizeX / 2
        return carX

    def centreCarY(self):
        carY = self.targetY - self.carSizeY / 2
        return carY

    def blitCar(self):
        mainWindow.blit(imageDictionary["redCar"], (self.centreCarX(), self.centreCarY()))

redCar = Car(30, 310, 40, 40)


# Music whatnot.
audioArray = ["breakingBad", "a-Ha", "daftPunk", "rickRoll", "polishCow"]
audioSelector = randint(0, 4)
mixer.Sound.play(audioDictionary[audioArray[audioSelector]])


# Game loop.
while gameRunning:
    for gameEvent in event.get():

        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False

        # Handles player movements.
        if gameEvent.type == KEYDOWN:

            # Up.
            if gameEvent.key == K_UP:
                bigPoppa.upMove()
            if gameEvent.key == K_w:
                bigPoppa.upMove()

            # Down.
            if gameEvent.key == K_DOWN:
                bigPoppa.downMove()
            if gameEvent.key == K_d:
                bigPoppa.downMove()

            # Left.
            if gameEvent.key == K_LEFT:
                bigPoppa.leftMove()
            if gameEvent.key == K_a:
                bigPoppa.leftMove()

            # Right.
            if gameEvent.key == K_RIGHT:
                bigPoppa.rightMove()
            if gameEvent.key == K_d:
                bigPoppa.rightMove()

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

    # Objects.
    bigPoppa.blitImage()
    redCar.blitCar()
    # Renders the game.
    display.flip()