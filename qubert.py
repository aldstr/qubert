import pycuber as pc
import time
from pycuber.solver import CFOPSolver


cube = pc.Cube()
alg = pc.Formula()
timesum = 0

for i in range(1, 100):
    rand = alg.random()
    cube(rand)
    cfopSolver = CFOPSolver(cube)
    start = time.process_time()
    solution = cfopSolver.solve(suppress_progress_messages=True)
    end = time.process_time()
    cfop_time = end - start
    print(cfop_time)
    timesum = timesum + cfop_time

avg_time = timesum / 100
print(avg_time)
