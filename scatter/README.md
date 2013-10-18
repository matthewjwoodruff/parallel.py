parallel
========
Make a parallel coordinate plot from the reference set solutions.
Also, generate data for AeroVis scatter plots.

- `parallel.py` does the parallel coordinate plotting
- `recalc.py` recomputes the objectives so we can compare ten- and three-objective solutions

This analysis was just enough to get the job done, so these scripts aren't pretty.

`recalc.py` hard-codes the location of the reference sets (sorry!)
`recalc.py` uses the Python GAA model from `generalaviation`.

## Invocation

````

python parkour.py ten 27_10_1.0.recalc 18_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 18 -c 0.8 0.0 0.2 0.9 -c 0.0 0.2 0.8 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2

python parkour.py three 27_3_0.1.recalc 18_3_0.1.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 18 -c 0.8 0.0 0.2 0.5 -c 0.0 0.2 0.8 0.5 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 1.5 1.5

python parkour.py eighteenten 18_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 18  -c 0.0 0.2 0.8 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2

python parkour.py twentyseventen 27_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 -c 0.8 0.0 0.2 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2
````
