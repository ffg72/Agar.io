import pygame
from pygame.math import Vector2

import core1 as core
from core1 import getMouseLeftClick


class Avatar:
    def __init__(self):
        self.taille = 10
        self.couleur = (255, 255, 0)
        self.position = Vector2(400, 400)
        self.vitesse = Vector2(0, 0)
        self.vitesseMin = Vector2(0, 0)
        self.vitesseMax = 2
        self.k = 0.01
        self.l0 = 1
        self.accMax = 0.5

    def affichage(self):
        core.Draw.circle(self.couleur, self.position, self.taille)

    def move(self, destination):
        if destination is not None:
            # bilan des forces
            # F=k * u * |l-l0|

            l = self.position.distance_to(destination)
            u = destination - self.position
            u = u.normalize()

            F = self.k * u * abs(l - self.l0) / self.taille


            # limiter la force max
            if F.length() > self.accMax:
                F.scale_to_length(self.accMax)

            # ajouter la force a la vitesse
            self.vitesse = self.vitesse + F

            # limiter la vitesse

            if self.vitesse.length() > self.vitesseMax-self.taille*0.05:
                self.vitesse.scale_to_length(self.vitesseMax-self.taille*0.05)

        # ajouter la vitesse a la position

        self.position = self.position + self.vitesse


    def bordure(self, fenetre):
        if self.position.y < 0:
            self.position.y = fenetre[1]

        #if

        '''if direction > 0 and self.position.x < core.WINDOW_SIZE[0] - self.taille.x:
            self.position.x += self.vitesse
        if direction < 0 and self.position.x > 0:
            self.position.x -= self.vitesse

        if direction > 0 and self.position.y < core.WINDOW_SIZE[1] - self.taille.y:
            self.position.y += self.vitesse
        if direction < 0 and self.position.y > 0:
            self.position.y -= self.vitesse
        '''



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