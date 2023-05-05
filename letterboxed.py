#!/bin/python3

def pairup(lst): return [a + b for a in lst for b in lst]


wordlist = "o3000.txt"

triples = [['a', 'b', 'c'],
           ['d', 'e', 'f'],
           ['g', 'h', 'i'],
           ['j', 'k', 'l']]

validletters = set(sum(triples, []))

solutions = [solution for solution in pairup(
    [word for word in open(wordlist, "r").read().split()
     if set(word) <= validletters
     and all([pair not in word for pair in sum(map(pairup, triples), [])])])
             if set(solution) == validletters
             and any(a == b for a, b in zip(solution, solution[1:]))]

print('\n'.join(solutions))
