from avatar1 import Avatar
import core
from creep import Creep


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1200, 850]


    print("Setup END-----------")
    core.memory("listeCreep", [])
    core.memory("avatar",Avatar())
    for c in range(99):
        core.memory("listeCreep").append(Creep())

def run():
    core.cleanScreen()
    for c in core.memory("listeCreep"):
        c.affichage(core.screen)

    core.memory("avatar").affichage()
    core.memory("avatar").move(core.getMouseLeftClick())


core.main(setup, run)
