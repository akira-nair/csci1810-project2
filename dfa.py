#!/usr/bin/env python
'''
File        :   dfa.py
Author      :   Akira Nair
Contact     :   akira_nair@brown.edu
Description :   Constructs a DFA that pattern-matches a string
'''

from dataclasses import dataclass
from kmp import failure_function
import sys

ALPHABET = ["A", "C", "G", "T"]
@dataclass
class DFA():
    states = []
    alphabet = []
    transitions = {}
    start = ""
    accept = []
    def render(self, file):
        out = \
        "digraph dfa {\n"+self.unpack_string()+"}"
        with open(file, 'w') as f:
            f.write(out)
        pass
    def unpack_string(self):
        out = ""
        for t in self.transitions:
            out += f"\t{t[0]} -> {self.transitions[t]} [label = \"{t[1]}\"]\n"""
        for s in self.accept:
            out += f"\t{s}[peripheries = 2]\n"
        return out

def construct_DFA(pattern):
    ff = failure_function(pattern)
    pattern_len = len(pattern)
    dfa = DFA()
    dfa.states = range(pattern_len+1)
    dfa.alphabet = ALPHABET
    dfa.accept = [dfa.states[pattern_len]]
    dfa.start = 0
    for j in range(1, pattern_len + 1):
        dfa.transitions[(j-1, pattern[j-1])] = j
    for a in dfa.alphabet:
        if a != pattern[0]:
            dfa.transitions[(0, a)] = 0
    for j in range(1, pattern_len):
        print(j)
        for a in dfa.alphabet:
            if a != pattern[j]:
                print(dfa.transitions)
                dfa.transitions[(j, a)] = dfa.transitions[ff[j], a]
    # print(dfa.transitions)
    return dfa

def read_file(filepath):
    with open(filepath) as f:
        return f.readline().strip()

def main(argv):
    dfa = construct_DFA(read_file(argv[0]))
    dfa.render(argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])


