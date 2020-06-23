# Buffon - a numerical experiment using Monte Carlo, Python and Postscript


Description:
-----------------------

We have two purposes here:

First thing is to have a Monte Carlo simulation example in Python. We implement Buffon's experiment where one estimates number $$\pi$$ by trowing a needle on a pattern made of parallel lines. Monte Carlo simulation evaluates an integral that appears in the process, by a numerical experiment.

The other thing we want to show is how to manipulate Postscript trough python programs, and create PS documents interactively.
A Post Script document made here is tailored specifically to plot results of Buffon needle experiment.

More specifically, we are merging Monte Carlo simulation example and the postscript functionality to produce a wonderful image found in a book by Werner Krauth -  Statistical Mechanics - Algorithms and Computation. The figure we make is a reconstruction of Fig. 1.10 in the book.

To run the example just type in shell (or just run the script):
```
python buffon.py

```
You will be prompted to enter the number of needles. To reproduce the image from the book I enter 2000:
```
Number of needles: 2000
Simulation over!
```
The result is a Postscript document 'buffon-experiment-fig'. You may convert it to PDF:
```
ps2pdf buffon-experiment-fig.ps
```

![The result of an experiment with 2000 needles/](https://github.com/nikola-m/Buffon/blob/master/buffon-experiment-fig.jpg)

