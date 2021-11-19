import random

import pygame
from pygame.math import Vector2


class Creep:
    def __init__(self):
        self.taille = 5
        self.couleur = (255, 0, 0)
        self.masse = 3
        self.position = Vector2(random.randint(0,1600),random.randint(0,850))


    def affichage(self,screen):

        pygame.draw.circle(screen, self.couleur, self.position, self.taille)






