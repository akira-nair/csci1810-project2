#!/usr/bin/env python
'''
File        :   dfa.py
Author      :   Akira Nair
Contact     :   akira_nair@brown.edu
Description :   Constructs a DFA that pattern-matches a string
'''

from dataclasses import dataclass
from kmp import failure_function

@dataclass
class DFA():
    states = []
    alphabet = []
    transitions = {}
    start = ""
    accept = []

def construct_DFA(pattern):
    ff = failure_function(pattern)
    pattern_len = len(pattern)
    dfa = DFA()
    dfa.states = range(pattern_len+1)
    dfa.alphabet = ["A", "C", "G", "T"]
    dfa.accept = [dfa.states[pattern_len]]
    for j in range(1, pattern_len + 1):
        dfa.transitions[(j-1, pattern[j-1])] = j
    for a in dfa.alphabet:
        if a != pattern[0]:
            dfa.transitions[(0, a)] = 0
    for j in range(1, pattern_len):
        print(j)
        for a in dfa.alphabet:
            if a != pattern[j]:
                dfa.transitions[(j-1, a)] = dfa.transitions[ff[j], a]
    #For j = 1 to l, for each a ∈ Σ and a ̸= pj+1, we have δ(j, a) = δ(f(j), a).
    # For each a ∈ Σ, a ̸= p1, we have δ(0, a) = 0.
    # For j = 1 to l, we have δ(j − 1, pj) = j.
    print(dfa.transitions)

def main():
    construct_DFA("AGGT")

if __name__ == "__main__":
    main()


