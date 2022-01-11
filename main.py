import pygame
from avatar1 import Avatar
import core
from creep import Creep


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1200, 850]

    #core.memory("centredecercle", [200, 200])
    #core.memory("rayonducercle", 10)
    #core.memory("couleurducercle", (255, 0, 0))

    print("Setup END-----------")

    core.memory("listeCreep",[])
    for c in range(0,99):
        core.memory("listeCreep").append(Creep())

def run():
    core.cleanScreen()
    for c in core.memory("listeCreep"):
        c.affichage(core.screen)

def affichage():
    Avatar.affichage(core.screen)


core.main(setup, run)
