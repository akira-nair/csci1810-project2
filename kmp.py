#!/usr/bin/env python
"""
File        :   kmp.py
Author      :   Akira Nair
Contact     :   akira_nair@brown.edu
Description :   Finds a pattern within a string
"""
import sys


def failure_function(pattern: str) -> dict:
    f = {}
    f[1] = 0
    i = 0
    for j in range(2, len(pattern) + 1):
        i = f[j - 1]
        while pattern[j - 1] != pattern[i] and i > 0:
            i = f[i]
        if pattern[j - 1] != pattern[i] and i == 0:
            f[j] = 0
        else:
            f[j] = i + 1
    return f


def match(pattern: str, text_substring: str) -> int:
    for i, symbol in enumerate(pattern):
        if symbol != text_substring[i]:
            return i + 1
    return 0


def kmp(pattern: str, text) -> int or list:
    if len(pattern) == 0 or len(text) == 0:
        return -1
    ff = failure_function(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    current_ind = 0
    matches = []
    while True:
        if current_ind + pattern_length > text_length:
            break

        mismatch = match(pattern, text[current_ind : current_ind + pattern_length])
        if mismatch == 0:
            matches.append(current_ind)
            ff_val = ff[pattern_length]
            current_ind += pattern_length - ff_val
        else:
            ff_val = ff[mismatch]
            if ff_val == 0:
                current_ind += 1
            else:
                current_ind += mismatch - ff_val
    if len(matches) > 0:
        return matches
    return -1


def read_file(filepath: str):
    with open(filepath) as f:
        text = f.readline().strip()
        pattern = f.readline().strip()
        return pattern, text


def main(argv):
    pattern, text = read_file(argv[0])
    print(kmp(pattern=pattern, text=text))


if __name__ == "__main__":
    main(sys.argv[1:])


"""

1: function Failure Function(p = p1 . . . pl)
2: f(1) ← 0
3: i ← 0
4: for j ∈ {2, . . . , l} do
5: i ← f(j − 1)
6: while pj ̸= pi+1 and i > 0 do
7: i ← f(i)
8: end while
9: if pj ̸= pi+1 and i = 0 then
10: f(j) ← 0
11: else
12: f(j) ← i + 1
13: end if
14: end for
15: end function


"""
