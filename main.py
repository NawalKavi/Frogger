# Initialising.
import pygame
from random import *

pygame.init()
pygame.font.init()
gameRunning = True
deathCount = 0
winCount = 0

# Game window parameters.
width = 320
height = 480
mainWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Chronicles of Big Poppa")


# Images.
imageDictionary = {
    "frog": pygame.transform.scale(pygame.image.load("Images//Frog.png"), (30, 30)),
    "frogWin": pygame.transform.scale(pygame.image.load("Images//Crowned Frog.png"), (35, 35)),
    "redCar": pygame.transform.scale(pygame.image.load("Images//Red Car.png"), (40, 40)),
    "blueBike": pygame.transform.scale(pygame.image.load("Images//Blue Bike.png"), (40, 40)),
    "background": pygame.transform.scale(pygame.image.load("Images//Background.png"), (320, 480)),
    "heart": pygame.transform.scale(pygame.image.load("Images//Heart.png"), (25, 25)),
    "log": pygame.transform.scale(pygame.image.load("Images//Log.png"), (100, 50)),
    "blackSquare": pygame.transform.scale(pygame.image.load("Images//Black.jpg"), (30, 30))
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


# Frog.
class Frog:

    def __init__(self, frogX, frogY):
        self.frogX = frogX
        self.frogY = frogY
        self.onLog = False
        self.drowning = None

    def currentX(self):
        return self.frogX

    def currentY(self):
        return self.frogY

    def upMove(self):
        if self.frogY > 80:
            if 0 < self.frogX < 40 or 75 < self.frogX < 130 or 160 < self.frogX < 215 or 215 < self.frogX < 300:
                self.frogY += 0
            if self.frogY < 75:
                self.frogY += 0
            else:
                self.frogY -= 2

    def downMove(self):
        if self.frogY < 445:
            self.frogY += 0
            if self.frogY < 75:
                self.frogY += 0
            else:
                self.frogY += 2

    def leftMove(self):
        if self.frogX >= 0:
            self.frogX += 0
            if self.frogY < 75:
                self.frogX += 0
            else:
                self.frogX -= 2

    def rightMove(self):
        if self.frogX <= 290:
            self.frogX += 0
            if self.frogY < 75:
                self.frogX += 0
            else:
                self.frogX += 2

    def winPosition(self):
        if self.frogY < 81:
            if 40 <= self.frogX <= 75:
                self.frogX = 60
                self.frogY = 55
        if self.frogY < 81:
            if 130 <= self.frogX <= 160:
                self.frogX = 145
                self.frogY = 55
        if self.frogY < 81:
            if 215 <= self.frogX <= 245:
                self.frogX = 230
                self.frogY = 55

    def moveFrogAway(self):
        if car1.collisionDetection() or car2.collisionDetection() or car3.collisionDetection():
            self.frogX = 310
            self.frogY = 55
    '''
        def standOnLog(self):
            if log1.collisionDetection():
                self.onLog = True
                self.frogX = log1.currentX()
                self.frogY = log1.currentY()
            elif log2.collisionDetection():
                self.onLog = True
                self.frogX = log2.currentX()
                self.frogY = log2.currentY()
            elif log3.collisionDetection():
                self.onLog = True
                self.frogX = log3.currentX()
                self.frogY = log3.currentY()
            else:
                self.onLog = False

            def drowningDetection(self):
                if 78 < self.frogX < 240:
                    if -1 < self.frogX < 291 and self.onLog == False:
                        return False
    '''
    def blitImage(self):
        mainWindow.blit(imageDictionary["frog"], (self.frogX, self.frogY))

bigPoppa1 = Frog(145, 415)
bigPoppa2 = Frog(145, 415)
bigPoppa3 = Frog(145, 415)


# Movement boolean.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False


# Vehicles.
class Car:

    def __init__(self, carX, carY, direction, speed):
        self.carX = carX
        self.carY = carY
        self.direction = direction
        self.speed = speed

    def keepMoving(self):
        if gameRunning:
            if self.direction == "Right":
                self.carX += self.speed
            if self.direction == "Left":
                self.carX -= self.speed

    def moveCarBack(self):
        if self.direction == "Right":
            if self.carX > 345:
                self.carX = -30
        if self.direction == "Left":
            if self.carX < -50:
                self.carX = 315

    def collisionDetection(self):
        if self.carX < bigPoppa1.currentX() < (self.carX + 40):
            if self.carY < bigPoppa1.currentY() < (self.carY + 40):
                return True
        if self.carX < bigPoppa2.currentX() < (self.carX + 40):
            if self.carY < bigPoppa2.currentY() < (self.carY + 40):
                return True
        if self.carX < bigPoppa3.currentX() < (self.carX + 40):
            if self.carY < bigPoppa3.currentY() < (self.carY + 40):
                return True

    def blitCar(self):
        if self.direction == "Left":
            mainWindow.blit(imageDictionary["blueBike"], (self.carX, self.carY))
        else:
            mainWindow.blit(imageDictionary["redCar"], (self.carX, self.carY))

car1 = Car(-30, 280, "Right", 2)
car2 = Car(335, 325, "Left", 4)
car3 = Car(-30, 370, "Right", 3)


# Logs.
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

    '''
        def collisionDetection(self):
            if self.logX < bigPoppa1.currentX() < (self.logX + 100):
                if self.logY < bigPoppa1.currentY() < (self.logY + 30):
                    return True
            if self.logX < bigPoppa2.currentX() < (self.logX + 100):
                if self.logY < bigPoppa2.currentY() < (self.logY + 30):
                    return True
            if self.logX < bigPoppa3.currentX() < (self.logX + 100):
                if self.logY < bigPoppa3.currentY() < (self.logY + 30):
                    return True
    '''

    def currentX(self):
        return self.logX

    def currentY(self):
        return self.logY

    def blitLog(self):
        mainWindow.blit(imageDictionary["log"], (self.logX, self.logY))

log1 = Log(-80, 100, 4, "Right")
log2 = Log(-80, 150, 1, "Right")
log3 = Log(350, 205, 2, "Left")


# Frame rate.
# Frame rate and text.
clock = pygame.time.Clock()
endText = pygame.font.SysFont("monospace", 42)


# Game loop.
while gameRunning:
    for gameEvent in pygame.event.get():

        # Quits game.
        if gameEvent.type == pygame.QUIT:
            gameRunning = False

        # Handles player movements.
        if gameEvent.type == pygame.KEYDOWN:

            # Up.
            if gameEvent.key == pygame.K_UP:
                moveUp = True
            if gameEvent.key == pygame.K_w:
                moveUp = True

            # Down.
            if gameEvent.key == pygame.K_DOWN:
                moveDown = True
            if gameEvent.key == pygame.K_s:
                moveDown = True

            # Left.
            if gameEvent.key == pygame.K_LEFT:
                moveLeft = True
            if gameEvent.key == pygame.K_a:
                moveLeft = True

            # Right.
            if gameEvent.key == pygame.K_RIGHT:
                moveRight = True
            if gameEvent.key == pygame.K_d:
                moveRight = True


        if gameEvent.type == pygame.KEYUP:

            # Up.
            if gameEvent.key == pygame.K_UP:
                moveUp = False
            if gameEvent.key == pygame.K_w:
                moveUp = False

            # Down.
            if gameEvent.key == pygame.K_DOWN:
                moveDown = False
            if gameEvent.key == pygame.K_s:
                moveDown = False

            # Left.
            if gameEvent.key == pygame.K_LEFT:
                moveLeft = False
            if gameEvent.key == pygame.K_a:
                moveLeft = False

            # Right.
            if gameEvent.key == pygame.K_RIGHT:
                moveRight = False
            if gameEvent.key == pygame.K_d:
                moveRight = False

            # Background music control.
            if gameEvent.key == pygame.K_p:
                pygame.mixer.pause()
            if gameEvent.key == pygame.K_u:
                pygame.mixer.unpause()

    # Initial Background.
    mainWindow.fill((0, 0, 0))

    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["background"], (0, 0))

    # River.
    river = pygame.draw.rect(mainWindow, (7, 11, 120), pygame.Rect(00, 90, 320, 157))

    # Log 1.
    log1.blitLog()
    '''
        log1.collisionDetection()
    '''
    log1.keepMoving()
    log1.moveLogBack()

    # Log 2.
    log2.blitLog()
    '''
        log2.collisionDetection()
    '''
    log2.keepMoving()
    log2.moveLogBack()

    # Log 3.
    log3.blitLog()
    '''
        log3.collisionDetection()
    '''
    log3.keepMoving()
    log3.moveLogBack()

    # Frog 1.
    bigPoppa1.blitImage()
    '''
        bigPoppa1.drowningDetection()
        bigPoppa1.standOnLog()
    '''
    bigPoppa1.winPosition()
    if moveUp:
        bigPoppa1.upMove()
    if moveDown:
        bigPoppa1.downMove()
    if moveRight:
        bigPoppa1.rightMove()
    if moveLeft:
        bigPoppa1.leftMove()
    if car1.collisionDetection() or car2.collisionDetection() or car3.collisionDetection():
        bigPoppa1.moveFrogAway()
        blitImage(imageDictionary["blackSquare"], (230, 5))
        deathCount += 1
    '''
        if log1.collisionDetection() or log2.collisionDetection() or log3.collisionDetection():
            bigPoppa1.standOnLog()
        if bigPoppa1.drowningDetection():
            bigPoppa1.moveFrogAway()
            blitImage(imageDictionary["blackSquare"], (230, 5))
            deathCount += 1
            print("collision")
    '''
    if bigPoppa1.frogY < 60:

        # Frog 2.
        bigPoppa2.blitImage()
        '''
            bigPoppa2.drowningDetection()
            bigPoppa2.standOnLog()
        '''
        bigPoppa2.winPosition()
        if moveUp:
            bigPoppa2.upMove()
        if moveDown:
            bigPoppa2.downMove()
        if moveRight:
            bigPoppa2.rightMove()
        if moveLeft:
            bigPoppa2.leftMove()
        if car1.collisionDetection() or car2.collisionDetection() or car3.collisionDetection():
            bigPoppa2.moveFrogAway()
            blitImage(imageDictionary["blackSquare"], (230, 5))
        '''
            if log1.collisionDetection() or log2.collisionDetection() or log3.collisionDetection():
                bigPoppa2.standOnLog()
            if bigPoppa2.drowningDetection():
                bigPoppa2.moveFrogAway()
                blitImage(imageDictionary["blackSquare"], (230, 5))
                deathCount += 1
                print("collision")
        '''
        if bigPoppa2.frogY < 60:

            # Frog 3.
            bigPoppa3.blitImage()
            '''
                bigPoppa3.drowningDetection()
                bigPoppa3.standOnLog()
            '''
            bigPoppa3.winPosition()
            if moveUp:
                bigPoppa3.upMove()
            if moveDown:
                bigPoppa3.downMove()
            if moveLeft:
                bigPoppa3.leftMove()
            if moveRight:
                bigPoppa3.rightMove()
            if car1.collisionDetection() or car2.collisionDetection() or car3.collisionDetection():
                bigPoppa3.moveFrogAway()
                blitImage(imageDictionary["blackSquare"], (230, 5))
                deathCount += 1
            '''
                if log1.collisionDetection() or log2.collisionDetection() or log3.collisionDetection():
                    bigPoppa3.standOnLog()
                if bigPoppa3.drowningDetection():
                    bigPoppa3.moveFrogAway()
                    blitImage(imageDictionary["blackSquare"], (230, 5))
                    deathCount += 1
                    print("collision")
            '''
    # Hearts.
    if deathCount == 0:
        blitImage(imageDictionary["heart"], (290, 5))
        blitImage(imageDictionary["heart"], (260, 5))
        blitImage(imageDictionary["heart"], (230, 5))
    if deathCount == 1:
        blitImage(imageDictionary["heart"], (290, 5))
        blitImage(imageDictionary["heart"], (260, 5))
    if deathCount == 2:
        blitImage(imageDictionary["heart"], (290, 5))

    # Cars.
    car1.blitCar()
    car1.collisionDetection()
    car1.keepMoving()
    car1.moveCarBack()

    car2.blitCar()
    car2.collisionDetection()
    car2.keepMoving()
    car2.moveCarBack()

    car3.blitCar()
    car3.collisionDetection()
    car3.keepMoving()
    car3.moveCarBack()

    # End screen.
    if bigPoppa1.frogY < 60 and bigPoppa2.frogY < 60 and bigPoppa3.frogY < 60:
        mainWindow.fill((0, 0, 0))
        displayText = endText.render("GAME OVER", 1, (255, 255, 255))
        mainWindow.blit(displayText, (50, 50))
    if deathCount >= 3:
        mainWindow.fill((0, 0, 0))
        displayText = endText.render("GAME OVER", 1, (255, 255, 255))
        mainWindow.blit(displayText, (50, 50))

    # Renders the game.
    pygame.display.flip()
    clock.tick(60)
