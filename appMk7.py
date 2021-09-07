import pygame
import math

pygame.init()
pygame.display.set_caption('Sub!')
screen = pygame.display.set_mode((850, 600))
clock = pygame.time.Clock()
bgColor = pygame.transform.smoothscale(pygame.image.load("grid.png"), (600,600))
compass = pygame.transform.smoothscale(pygame.image.load("compass2.png"), (250,250))
shipBearing = 0
shipX, shipY = 300,300
shipV = 1
turningspeed = 1

def convertToRadians( bearing ):
    return bearing * (math.pi / 180)

def findChange( bearingDegrees, velocity ):
    # return an x and y change
    if bearingDegrees == 0:
        return (0,-velocity) # heading straight up, note we're not using Cartesian coords
    elif bearingDegrees < 90: # in Q1
        return (math.sin(convertToRadians(bearingDegrees)) * velocity, math.cos(convertToRadians(bearingDegrees)) * -velocity)
    elif bearingDegrees == 90: # heading directly right
        return (velocity,0)
    elif bearingDegrees < 180: # in Q4
        angleToHorizontal = bearingDegrees - 90
        return (math.cos(convertToRadians(angleToHorizontal)) * velocity, math.sin(convertToRadians(angleToHorizontal)) * velocity)
    elif bearingDegrees == 180: # heading directly down, note we're not using Cartesian coords
        return (0,velocity)
    elif bearingDegrees < 270: # in Q3
        angleToHorizontal = 270 - bearingDegrees
        return (math.cos(convertToRadians(angleToHorizontal)) * -velocity, math.sin(convertToRadians(angleToHorizontal)) * velocity)
    elif bearingDegrees == 270: # heading directly left
        return (-velocity,0)
    elif bearingDegrees < 360: # in Q2
        angleToHorizontal = bearingDegrees - 270
        return (math.cos(convertToRadians(angleToHorizontal)) * -velocity, math.sin(convertToRadians(angleToHorizontal)) * -velocity)

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    


image = pygame.image.load('Ship3.png')
pointer = pygame.image.load('point1.png')
w, h = image.get_size()
angle = 0

run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    pos = (shipX, shipY)
    pos1 = (703.9, 18)
    screen.blit(bgColor, (0,0))    
    blitRotate(screen, image, pos, (w/2, h/2), angle)    
    screen.blit(compass, (600,0))
    blitRotate2(screen, pointer, pos1, angle)


    if keys[pygame.K_RIGHT]:
        angle -= turningspeed
        shipBearing = (shipBearing + turningspeed) % 360
        # print("turn right")
    if keys[pygame.K_LEFT]:
        angle += turningspeed
        shipBearing = (shipBearing - turningspeed) %360 
        # print("turn left")

    if keys[pygame.K_UP]:
        if keys[pygame.K_SPACE]:
            shipV = 3
        dx, dy = findChange( shipBearing, shipV )
        shipX += dx
        shipY += dy
        shipV = 1
    

    if shipX <= 0:
        shipX = 0
    elif shipX >= 600:
        shipX = 600
    if shipY <= 0:
        shipY = 0
    elif shipY >= 600:
        shipY = 600 
       


    pygame.display.flip()

pygame.quit()
exit()