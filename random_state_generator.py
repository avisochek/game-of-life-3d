## For now this is just a copy and paste function that generates a
## completely random state based on a probability that a cell is 'living'

## Future versions may integrate this into more high level features
import random
def random_state(probs,x,y,z):
    state = set([])
    for i in range(x):
        for j in range(y):
            for k in range(Z):
                if random.random < probs:
                    state.add((x,y,z))
    return state
