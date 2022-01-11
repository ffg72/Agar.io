import pygame
from pygame.math import Vector2

from core import getMouseLeftClick


class Avatar:
    def __init__(self):
        self.taille = 8
        self.couleur = (255, 255, 255)
        self.masse = 5
        self.position = Vector2(400,450)
        self.vitesse = Vector2(0,0)
        self.vitesseMin = Vector2(0,0)
        self.vitesseMax = Vector2(0,0)


    def affichage(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.taille)

    def move(self, screen):

        dX, dY = pygame.mouse.get_pos()
        # Find the angle from the center of the screen to the mouse in radians [-Pi, Pi]
        rotation = math.atan2(dY - float(SCREEN_HEIGHT)/2, dX - float(SCREEN_WIDTH)/2)
        # Convert radians to degrees [-180, 180]
        rotation *= 180/math.pi
        # Normalize to [-1, 1]
        # First project the point from unit circle to X-axis
        # Then map resulting interval to [-1, 1]
        normalized = (90 - math.fabs(rotation))/90
        vx = self.vitesse*normalized
        vy = 0
        if rotation < 0:
            vy = -self.vitesse + math.fabs(vx)
        else:
            vy = self.vitesse - math.fabs(vx)
        tmpX = self.x + vx
        tmpY = self.y + vy
        self.x = tmpX
        self.y = tmpY


    def deplacer(self, direction, core):

        getMouseLeftClick()

        if direction > 0 and self.position.x < core.WINDOW_SIZE[0] - self.taille.x:
            self.position.x += self.vitesse
        if direction < 0 and self.position.x > 0:
            self.position.x -= self.vitesse

        if direction > 0 and self.position.y < core.WINDOW_SIZE[0] - self.taille.y:
            self.position.y += self.vitesse
        if direction < 0 and self.position.y > 0:
            self.position.y -= self.vitesse


    def setVitesse(self, v):
            self.vitesse = v

    def setPosition(self, pos):
        self.position = pos

    def getVitesse(self):
        return self.vitesse

    def getPosition(self):
        return self.position

    def getTaille(self):
        return self.taille