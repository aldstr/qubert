import pycuber as pc
from pycuber.solver import CFOPSolver

c = pc.Cube()
alg = pc.Formula()
i = 0;
while i<100:
    random_alg = alg.random()
    c(random_alg)
    solver = CFOPSolver(c)
    solution = solver.solve(suppress_progress_messages=True)
    print(i)
    print(solution)
    i = i+1
