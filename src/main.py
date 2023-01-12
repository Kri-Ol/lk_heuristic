import tsplib95
from lk_heuristic.utils.solver_funcs import solve

print('start')

# tsp_file="C:/Users/kriol/Source/Repos/LKHWin-2.0.10/lk_heuristic/src/lk_heuristic/samples/a280.tsp",
# tsp_file="C:/Users/kriol/Documents/Python/lk_heuristic/src/lk_heuristic/samples/a280.tsp"
solve(tsp_file="C:/Users/kriol/Documents/Python/lk_heuristic/src/lk_heuristic/samples/a280.tsp",
      solution_method="lk2_improve",
      runs=50,
      backtracking=(5, 5),
      reduction_level=4,
      reduction_cycle=4,
      logging_level=20)

print('end')
