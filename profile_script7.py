import cProfile
import pstats

cProfile.run("import main", "stats")
p = pstats.Stats("stats")
p.sort_stats("cumtime").print_stats("/app/main.py")
