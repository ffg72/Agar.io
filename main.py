import pygame

import core1 as core
from avatar1 import Avatar
from creep import Creep
from ennemis1 import Ennemis



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1000, 650]

    print("Setup END-----------")

    core.memory("listeCreep", [])
    core.memory("avatar",Avatar())
    core.memory("ennemis",Ennemis())

    for c in range(99):
        core.memory("listeCreep").append(Creep())
        print(core.memory("listeCreep"), [c])

def run():
        core.cleanScreen()
        for c in core.memory("listeCreep"):
            c.affichage(core.screen)

        core.memory("avatar").affichage()
        core.memory("avatar").move(core.getMouseLeftClick())
        core.memory("ennemis").affichage()
        core.memory("ennemis").move(core.memory("avatar").position)
        #core.memory("ennemis").fuir("avatar")

        for c in core.memory("listeCreep"):
            c.collision(core.memory("ennemis"))
            c.collision(core.memory("avatar"))


        if core.getKeyPressList(27):
            pygame.quit()

#print(core.keyPressValue)

core.main(setup,run)
