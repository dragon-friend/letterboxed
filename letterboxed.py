#!/bin/python3

from functools import reduce


def pairup(lst): return [a + b for a in lst for b in lst]
def concat(a, b): return a + b


wordlist = "o300.txt"

triples = [['e', 'i', 'o'],
           ['m', 'c', 't'],
           ['l', 'a', 'h'],
           ['p', 'y', 'u']]

validletters = set(reduce(concat, triples, []))

solutions = [solution for solution in pairup(
    [word for word in open(wordlist, "r").read().split()
     if set(word) <= validletters
     and all([pair not in word for pair in
              reduce(concat, map(pairup, triples), [])])])
             if set(solution) == validletters
             and any(a == b for a, b in zip(solution, solution[1:]))]

print('\n'.join(solutions))
