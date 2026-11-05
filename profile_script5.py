import cProfile
import pstats
import os

cProfile.run("import main", "stats")
p = pstats.Stats("stats")
p.sort_stats("cumtime").print_stats("main.py")
