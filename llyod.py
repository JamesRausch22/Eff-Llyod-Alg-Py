import math
import numpy as np
from random import randint
k = 2
points = [[1.3, 1.1], [1.3, 0.2], [0.6, 2.8], [3.0, 3.2], [1.2, 0.7], [1.4, 1.6], [1.2, 1.0], [1.2, 1.1], [0.6, 1.5], [1.8, 2.6], [1.2, 1.3], [1.2, 1.0], [0.0, 1.9]]
def ed(x, y): return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))
def target(): return randint(0, len(points) - 1)
def equiv(x, y): return x == y
def fill(x): x.append([])
def run():
    centers = []
    for i in range(1, k+1):
		centers.append(points[target()])
    while(True):
        clusters = []
        for i in range(k):
            fill(clusters)
        for p in points:
            cC = [0, ed(p, centers[0])]
            for i in range(1, k):
		dif = ed(p, centers[1])
		if(dif < cC[1]):
                    cC = [i , dif]
        	clusters[cC[0]].append(p)
        nC = []
        def ncA(x): x.append(np.mean(clusters[i], axis=0).tolist())
        for i in range(k):
            ncA(nC)
        change = False
        for i in range(k):
            if equiv(centers[i], nC[i]) == False:
                change = True
        centers = nC
        if(change == False):
            print(nC)
            break
run()
