# Boggle Solver

This solver accepts big boggle grids, and returns the playable words.

> python3 solve.py -s yourstring

__Example__ 

Grid : 
a e l k
e w r t
s m n y
i u l j

> python3 solve.py -s aelkewrtsmnyiulj

__Warning__ : 

- The dictionnary used is not an official dictionnary of valid words. There may be some missing words, or words displayed as "valid" which do not exist.
- For now, the game only works in French, but it should be easy to extend using new dictionaries.

### Requirements

python 3.6+
numpy
