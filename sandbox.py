## !sandbox.py:
## experimental implementation of game of life 3d and notes
import random
#from vpython import *
from world import World

def random_state(probs,x,y,z):
    state = set([])
    for i in range(x):
        for j in range(y):
            for k in range(z):
                num = random.random()
                if num < probs:
                    state.add((x,y,z))
    return state



world = World(seed=random_state(0.1,10,10,10))
for i in range(100):
    world.update()
