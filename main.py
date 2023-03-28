# Initialising.
import pygame
from random import *
pygame.init()
gameRunning = True

# Game window parameters.
width = 320
height = 480
mainWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Chronicles of Big Poppa")


# Images.
imageDictionary = {
    "frog": pygame.transform.scale(pygame.image.load("Images//Frog.png"), (30, 30)),
    "frogWin": pygame.transform.scale(pygame.image.load("Images//Crowned Frog.png"), (35, 35)),
    "blueBike": pygame.transform.scale(pygame.image.load("Images//Blue Bike.png"), (40, 40)),
    "redCar": pygame.transform.scale(pygame.image.load("Images//Red Car.png"), (40, 40)),
    "background": pygame.transform.scale(pygame.image.load("Images//Background.png"), (320, 480)),
    "heart": pygame.transform.scale(pygame.image.load("Images//Heart.png"), (25, 25)),
    "log": pygame.transform.scale(pygame.image.load("Images//Log.png"), (100, 50))
}

# Blitting or something.
def blitImage(imageAddress, xyValues):
    mainWindow.blit(imageAddress, xyValues)


# Audio.
audioDictionary = {
    "breakingBad": pygame.mixer.Sound("Audio//Breaking Bad Theme Song (8 Bit).mp3"),
    "a-Ha": pygame.mixer.Sound("Audio//Take On Me (8 Bit).mp3"),
    "daftPunk": pygame.mixer.Sound("Audio//Harder Better Faster Stronger (8 Bit).mp3"),
    "rickRoll": pygame.mixer.Sound("Audio//Never Gonna Give You Up (8 Bit).mp3"),
    "polishCow": pygame.mixer.Sound("Audio//Polish Cow (8 Bit).mp3"),
    "downUnder": pygame.mixer.Sound("Audio//Down Under (8 Bit).mp3")
}

# Music whatnot.
audioArray = ["breakingBad", "a-Ha", "daftPunk", "rickRoll", "polishCow", "downUnder"]
audioSelector = randint(0, 4)
pygame.mixer.Sound.play(audioDictionary[audioArray[audioSelector]])


class Frog:

    def __init__(self, frogX, frogY):
        self.frogX = frogX
        self.frogY = frogY

    def upMove(self):
        if self.frogY >= 25:
            self.frogY -= 30
        print("Frog Y:", self.frogY)

    def downMove(self):
        if self.frogY <= 440:
            self.frogY += 30
        print("Frog Y:", self.frogY)

    def leftMove(self):
        if self.frogX >= 25:
            self.frogX -= 30
        print("Frog X:", self.frogX)

    def rightMove(self):
        if self.frogX <= 275:
            self.frogX += 30
        print("Frog X:", self.frogX)

    def drowningDetection(self):
        if self.frogY:
            pass

    def blitImage(self):
        mainWindow.blit(imageDictionary["frog"], (self.frogX, self.frogY))

bigPoppa = Frog(145, 415)


class Car:

    def __init__(self, carX, carY):
        self.carX = carX
        self.carY = carY

    def keepMoving(self):
        if gameRunning:
            self.carX += 15

    def moveCarBack(self):
        if self.carX > 345:
            self.carX = -30

    def blitCar(self):
        mainWindow.blit(imageDictionary["redCar"], (self.carX, self.carY))

car = Car(-30, 280)


class Bike:

    def __init__(self, bikeX, bikeY, direction):
        self.bikeX = bikeX
        self.bikeY = bikeY
        self.direction = direction

    def keepMoving(self):
        if gameRunning:
            if self.direction == "Right":
                self.bikeX += 10
            if self.direction == "Left":
                self.bikeX -= 8

    def moveBikeBack(self):
        if self.direction == "Right":
            if self.bikeX > 345:
                self.bikeX = -30
        if self.direction == "Left":
            if self.bikeX < -50:
                self.bikeX = 315

    def blitBike(self):
        mainWindow.blit(imageDictionary["blueBike"], (self.bikeX, self.bikeY))

bike1 = Bike(335, 325, "Left")
bike2 = Bike(-30, 370, "Right")


class Log:

    def __init__(self, logX, logY, speed, direction):
        self.logX = logX
        self.logY = logY
        self.speed = speed
        self.direction = direction

    def keepMoving(self):
        if gameRunning:
            if self.direction == "Right":
                self.logX += self.speed
            if self.direction == "Left":
                self.logX -= self.speed

    def moveLogBack(self):
        if self.direction == "Right":
            if self.logX > 355:
                self.logX = -80
        if self.direction == "Left":
            if self.logX < -90:
                self.logX = 350

    def blitLog(self):
        mainWindow.blit(imageDictionary["log"], (self.logX, self.logY))

log1 = Log(-80, 100, 9, "Right")
log2 = Log(-80, 150, 5, "Right")
log3 = Log(350, 205, 12, "Left")


# Game loop.
clock = pygame.time.Clock()
while gameRunning:
    for gameEvent in pygame.event.get():

        # Quits game.
        if gameEvent.type == pygame.QUIT:
            gameRunning = False

        # Handles player movements.
        if gameEvent.type == pygame.KEYDOWN:

            # Up.
            if gameEvent.key == pygame.K_UP:
                bigPoppa.upMove()
            if gameEvent.key == pygame.K_w:
                bigPoppa.upMove()

            # Down.
            if gameEvent.key == pygame.K_DOWN:
                bigPoppa.downMove()
            if gameEvent.key == pygame.K_s:
                bigPoppa.downMove()

            # Left.
            if gameEvent.key == pygame.K_LEFT:
                bigPoppa.leftMove()
            if gameEvent.key == pygame.K_a:
                bigPoppa.leftMove()

            # Right.
            if gameEvent.key == pygame.K_RIGHT:
                bigPoppa.rightMove()
            if gameEvent.key == pygame.K_d:
                bigPoppa.rightMove()

            # Background music control.
            if gameEvent.key == pygame.K_p:
                pygame.mixer.pause()
            if gameEvent.key == pygame.K_u:
                pygame.mixer.unpause()

    # Initial Background.
    mainWindow.fill((0, 0, 0))

    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["background"], (0, 0))

    # Hearts.
    blitImage(imageDictionary["heart"], (290, 5))
    blitImage(imageDictionary["heart"], (260, 5))
    blitImage(imageDictionary["heart"], (230, 5))

    # River.
    pygame.draw.rect(mainWindow, (7, 11, 120), pygame.Rect(00, 90, 320, 157))

    # Objects.
    bigPoppa.blitImage()

    # Car.
    car.blitCar()
    car.keepMoving()
    car.moveCarBack()

    # Bike 1.
    bike1.blitBike()
    bike1.keepMoving()
    bike1.moveBikeBack()

    # Bike 2.
    bike2.blitBike()
    bike2.keepMoving()
    bike2.moveBikeBack()

    # Log 1.
    log1.blitLog()
    log1.keepMoving()
    log1.moveLogBack()

    # Log 2.
    log2.blitLog()
    log2.keepMoving()
    log2.moveLogBack()

    # Log 3.
    log3.blitLog()
    log3.keepMoving()
    log3.moveLogBack()

    # Renders the game.
    pygame.display.flip()
    clock.tick(15)