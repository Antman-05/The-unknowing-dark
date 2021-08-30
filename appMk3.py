  
import pygame, random

WIDTH = 600
HEIGHT = 600
BORDER = 20
FRAMERATE = 120
P_VELOCITY = 1

pygame.init()
pygame.display.set_caption('Sub!')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bgColor = pygame.transform.smoothscale(pygame.image.load("grid.png"), (600,600))
screen.blit(bgColor, (-1,-1))
clock = pygame.time.Clock()


class Ship():
    def __init__(self, pImg, pX, pY, p_dX, p_dY):
        self.img = pImg
        self.x = pX
        self.y = pY
        self.dx = p_dX
        self.dy = p_dY
    def update(self):
        self.x += self.dx
        # ensure the player doesn't leave the screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
    def show(self):
        global screen
        screen.blit(self.img, (self.x,self.y))
        
p1 = Ship(pygame.image.load('Ship3.png'),220,220,0,0)

running = True
while running:
    screen.fill((0,0,0))        #prevents doubles of sprite forming, deletes images as it goes. 
    screen.blit(bgColor, (0,0)) #redraws grid every time screen is wiped. 
 
    for event in pygame.event.get():
        # this is to close the window
        if event.type == pygame.QUIT:
            running = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the keys being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                # print("Left pressed")
                p1.dx = -P_VELOCITY
            if event.key == ord('d'):
                # print("Right pressed")
                p1.dx = P_VELOCITY
        if event.type == pygame.KEYUP:
            if event.key == ord('a'): 
                # print("Left or right released")
                p1.dx = 0
            if event.key == ord('d'):
                p1.dx = 0
        # we update the screen at every frame
        
    # if we put the frame rate at 60 the sprite will move slower

    clock.tick( FRAMERATE )
    p1.update()
    p1.show()
    pygame.display.update()