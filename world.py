import numpy as np

# rilt = remove_if_less_than, etc...

class World():
    def __init__(self, seed, x=10,y=10,z=10, rilt=4, rigt=10, ailt=0, aigt=4):
        self.x = x
        self.y = y
        self.z = z
        self.generation = 0
        self.state = seed
        self.rilt = rilt
        self.rigt = rigt
        self.ailt = ailt
        self.aigt = aigt
    def update(self):
        neighbor_counts={}
        for cell in self.state:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        cx = cell[0]+i
                        cy = cell[1]+j
                        cz = cell[2]+k
                        valid_cell = not ((i==0) and (j==0) and (k==0))
                        valid_cell &= (cx>=0 and cy>=0 and cz>=0)
                        valid_cell &= (cx<self.x and cy<self.y and cz<self.z)
                        if valid_cell:
                            neighbor = (cx, cy, cz)
                            if not neighbor in neighbor_counts:
                                neighbor_counts[neighbor]=1
                            else:
                                neighbor_counts[neighbor]+=1
        for cell, count in neighbor_counts.items():
            if not cell in self.state:
                if (count < self.ailt) or (count > self.aigt):
                    self.state.add(cell)
            elif (count > self.rilt) or (count > self.rigt):
                self.state.remove(cell)
        self.generation += 1
