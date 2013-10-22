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

python parallel.py ten 27_10_1.0.recalc 18_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 18 -c 0.8 0.0 0.2 0.9 -c 0.0 0.2 0.8 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2

python parallel.py three 27_3_0.1.recalc 18_3_0.1.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 18 -c 0.8 0.0 0.2 0.5 -c 0.0 0.2 0.8 0.5 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 1.5 1.5

python parallel.py eighteenten 18_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 18  -c 0.0 0.2 0.8 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2

python parallel.py twentyseventen 27_10_1.0.recalc -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 -c 0.8 0.0 0.2 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2

python parallel.py eighteenten_objectives 18_10_1.0.recalc -C 54-63 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 18 -c 0.0 0.2 0.8 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.4 0.4

python parallel.py twentyseventen_objectives 27_10_1.0.recalc -C 54-63 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 -c 0.8 0.0 0.2 0.9 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.4 0.4

python parallel.py ten_objectives 27_10_1.0.recalc 18_10_1.0.recalc -C 54-63 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n 27 18 -c 0.8 0.0 0.2 0.9 -c 0.0 0.2 0.8 0.9 -m 73.3 1880 60 1.81 360 42000 -2650 -17.2 -204 0.3 -M 74.0 2020 80 2.00 500 45000 -2000 -14.6 -190 2.2 -W 0.7 0.7

(sent to Pat)
python parallel.py all 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 1.0 0.0 0.0 1.0 -c 0.0 0.0 1.0 1.0 -c 0.5 0.5 0.0 1.0 -c 0.0 0.5 0.5 1.0 -c 1.0 0.0 0.0 1.0 -c 0.0 0.0 1.0 1.0 -c 0.5 0.5 0.0 1.0 -c 0.0 0.5 0.5 1.0 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.2 0.4 0.4 1 1 1 1 -k '-' '-' '-' '-' 'o' 'v' '^' '<' -z 0 0 1 1 2 2 2 2

python parallel.py all_objectives 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 54-66 -w 13 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 0.1 0.1 0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF F1 F2 F3 -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 1.0 0.0 0.0 1.0 -c 0.0 0.0 1.0 1.0 -c 0.5 0.5 0.0 1.0 -c 0.0 0.5 0.5 1.0 -c 1.0 0.0 0.0 1.0 -c 0.0 0.0 1.0 1.0 -c 0.5 0.5 0.0 1.0 -c 0.0 0.5 0.5 1.0 -m 73.1 1880 55 1.80 360 42000 -2650 -17.2 -206 0.2 86 -156.5 0.2 -M 74.1 2020 80 2.00 500 45000 -2000 -14.6 -190 2.2 96 -142.0 2.2 -W 0.2 0.2 0.4 0.4 1 1 1 1 -k '-' '-' '-' '-' 'o' 'v' '^' '<' -z 0 0 1 1 2 2 2 2

(Tweaked, script upgrade to white outlines on markers)
python parallel.py all 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 0.3 0.0 0.0 1.0 -c 0.3 0.3 1.0 1.0 -c 0.6 0.6 0.0 1.0 -c 0.0 0.8 0.8 1.0 -c 0.3 0.0 0.0 1.0 -c 0.3 0.3 1.0 1.0 -c 0.6 0.6 0.0 1.0 -c 0.0 0.8 0.8 1.0 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.2 0.5 0.7 0.7 0.8 0.8 0.8 0.8 -k '-' '-' '-' '-' 'o' 's' 'o' 's' -z 0 0.1 2 2 3 3 3 3

Different color scheme: dark and in back, with square markers, for 27 DVs.  Light and in front, with circles, for 18 DVs

python parallel.py all 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 0.5 0.0 0.0 1.0 -c 0.2 0.2 1.0 1.0 -c 1.0 0.5 0.5 1.0 -c 0.8 0.8 1.0 1.0 -c 0.5 0.0 0.0 1.0 -c 0.2 0.2 1.0 1.0 -c 1.0 0.5 0.5 1.0 -c 0.8 0.8 1.0 1.0 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.3 0.5 0.7 0.7 0.8 0.8 0.8 0.8 -k '-' '-' '-' '-' 's' 's' 'o' 'o' -z 0 0.1 2 2 3 3.1 4 4

Tweaked color scheme, for use with comically large markers:
python parallel.py all 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.5 0.7 0.8 0.8 0.1 1.2 1.0 1.0 -k '-' '-' '-' '-' 's' 's' 'o' 'o' -z 0 0.2 2 3 4 4.1 5 6

python parallel.py all 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 27-35 63 36-44 63 45-53 63 -w 10 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -m 73.2 1820 55 1.78 280 41000 -2680 -17.3 -206 0.2 -M 74.2 2040 80 2.00 500 45000 -2000 -14.4 -186 2.3 -W 0.5 0.7 0.8 0.8 0.1 1.2 1.0 1.0 -k '-' '-' '-' '-' 's' 's' 'o' 'o' -z 0 0.2 2 3 4 4.1 5 6

python parallel.py all_objectives 27_10_1.0.recalc 18_10_1.0.recalc 27_3_0.1.recalc 18_3_0.1.recalc 27_10_1.0.minima 18_10_1.0.minima 27_3_0.1.minima 18_3_0.1.minima -C 54-66 -w 13 -p 0.1  20  1  0.01  20  1000  40  0.1  2  0.1 0.1 0.1 0.1 -a NOISE WEMP DOC ROUGH WFUEL PURCH RANGE LDMAX VCMAX PFPF F1 F2 F3 -n '27 10' '18 10' '27 3' '18 3' '27 10' '18 10' '27 3' '18 3'  -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -c 0.5 0.0 0.0 1.0 -c 0.4 0.8 1.0 1.0 -c 1.0 0.6 0.6 1.0 -c 0.8 1.0 1.0 1.0 -m 73.1 1880 55 1.80 360 42000 -2650 -17.2 -206 0.2 86 -156.5 0.2 -M 74.1 2020 80 2.00 500 45000 -2000 -14.6 -190 2.2 96 -142.0 2.2 -W 0.5 0.7 0.8 0.8 0.1 1.2 1.0 1.0 -k '-' '-' '-' '-' 's' 's' 'o' 'o' -z 0 0.2 2 3 4 4.1 5 6
````

## Comment

* Who:	People who use MOEAs for design optimization, or are considering using them for that purpose
* What:	Parallel coordinate plot showing model outputs for all three aircraft, for all four problem formulations.  Z ordering puts 10-objective solutions behind 3-objective solutions.  Dark colors are for ten objectives and light colors are for three objectives.  Reds are for 27 DVs and blues are for 18 DVs.
* When: First thing after optimization, once the data are in a consistent format
* Where: MOVA, inselberg, anybody who might make the claim that reducing the decision space makes the problem easier
* Why:	 Because MOVA, we want to have a broad range of alternatives, and that means that superior performance is only half the story, the other half being that the *inferior* performance on some axes is also good because it means that we're able to trade off that specific attribute for dominance elsewhere.
* How:  Each MOEA is sorted to produce a refset and then those refsets are sorted together to produce a refset for each problem.  Then parallel coord plot is done using parallel.py.
