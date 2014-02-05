g6602-hacks
===========
Central repo for work done on G6602 Spring 2014 at Columbia

## turtle_times.py

Usage:

python turtle_times.py [somefile]

Where somefile is a textfile containing the body text of some news story. Watch as Frank turtle "interprets" the news. See code for implementation comments.

If somefile is not given, the program reads from stdin (Ctrl-D to end input).

This script outputs a record of the turtle's otherwise transient scribbles to a file out.eps in the same directory.

## monkey.py

Naive infinite monkey implementation. Maximizes on cardinality of common substrings - don't know how good this is, it certainly won't achieve the target.

## monkey_hill_climbing.py

Infinite monkey with incremental improvement, mutates one non-correct character per iteration. Maximizes on correct chars in correct position.

(Python 3)

## aftersol.py

After Sol Lewitt. Uses TkInter which is a standard module to draw on a canvas. Would like to expand this to include user input "ratifying" mutations. 
