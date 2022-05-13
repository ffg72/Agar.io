import random
from pygame.math import Vector2
import core1
from core1 import getMouseLeftClick
import avatar1 as avatar

class Ennemis:
    def __init__(self):
        self.taille = 10
        self.couleur = (255, 255, 0)
        self.masse = 5
        self.position = Vector2(500, 500)
        self.vitesse = Vector2(0, 0)
        self.vitesseMin = Vector2(0, 0)
        self.vitesseMax = 2
        self.k = 0.01
        self.l0 = 1
        self.accMax = 0.5
        self.target = Vector2(0, 0)


    def affichage(self):
        core1.Draw.circle(self.couleur, self.position, self.taille)

    def move(self, destination):
        if destination is not None:
            # bilan des forces
            # F=k * u * |l-l0|

            l = self.position.distance_to(destination)
            u = destination - self.position
            u = u.normalize()

            F = self.k * u * abs(l - self.l0) / self.taille
            #print(F)

            # limiter la force max
            if F.length() > self.accMax:
                F.scale_to_length(self.accMax)

            # ajouter la force a la vitesse
            self.vitesse = self.vitesse + F

            # limiter la vitesse
            if self.vitesse.length() > self.vitesseMax - self.taille * 0.05:
                self.vitesse.scale_to_length(self.vitesseMax - self.taille * 0.05)

        # ajouter la vitesse a la position

        self.position = self.position + self.vitesse


    def deplacer(self, direction, core):
        if direction > 0 and self.position.x < core.WINDOW_SIZE[0] - self.taille.x:
            self.position.x += self.vitesse
        if direction < 0 and self.position.x > 0:
            self.position.x -= self.vitesse

        if direction > 0 and self.position.y < core.WINDOW_SIZE[0] - self.taille.y:
            self.position.y += self.vitesse
        if direction < 0 and self.position.y > 0:
            self.position.y -= self.vitesse

    def manger(self, creep):
        if creep.position.distance_to(self.position) < self.taille + creep.taille:
            self.taille = creep.taille + self.taille
            creep.position = Vector2(random.randint(0, 1600), random.randint(0, 850))
            creep.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            print(self.taille)

    #def fuir(self,avatar):
        #if self.taille < avatar.getTaille() and self.distance(avatar) < 200:
            #point = Vector2(self.position.x - avatar.getPosition().x, self.position.y - avatar.getPosition().y)
            #self.target = self.position + point
            #self.position.x = Vector2(random.randint(0,700),random.randint(0,700))

            #point = Vector2(self.position.x - avatar.getPosition().x, self.position.y - avatar.getPosition().y)
            #self.target = self.position + point
            #print(self.position)

    #def comportement(self, avatar):
        #if avatar.getTaille() > self.taille and self.distance(avatar) < 200:
        #self.fuir(avatar)

        #elif avatar.getTaille() < self.taille:
        #   self.mangerJoueur(avatar)

    def distance(self, avatar):
        return Vector2(self.position.x - avatar.getPosition().x, self.position.y - avatar.getPosition().y).magnitude()

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