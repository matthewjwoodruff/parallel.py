parallel
========
Make a parallel coordinate plot from the reference set solutions.
Also, generate data for AeroVis scatter plots.

- `parallel.py` does the parallel coordinate plotting
- `recalc.py` recomputes the objectives so we can compare ten- and three-objective solutions

This analysis was just enough to get the job done, so these scripts aren't pretty.

`recalc.py` hard-codes the location of the reference sets (sorry!)
`recalc.py` uses the Python GAA model from `generalaviation`.
