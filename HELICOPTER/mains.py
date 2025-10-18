from pynput import keyboard
from map import Map
from helicopter import Helicopter as Helico
import time
import os

TICK_SLEEP = 0.2
TREE_UPDATE = 40
FIRE_UPDATE = 20
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

field.generate_forest(3, 10)
field.generate_river(10)
field.generate_river(10)
field.generate_river(10)

tick = 1

MOVES = {'w': (-1,0), 'd': (0,1), 's': (1,0), 'a': (0,-1)}

def proccess_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)

listener = keyboard.Listener(
    on_press=None,
    on_release=proccess_key)
listener.start()


while True:
    os.system('cls')
    field.processHelico(helico)
    helico.printStats()
    field.print_map(helico)
    print('Tick', tick)
    tick += 1
    time.sleep(TICK_SLEEP)

    if (tick % TREE_UPDATE == 0):
        field.generate_tree()

    if (tick % FIRE_UPDATE == 0):
        field.update_fire()

