#!/usr/bin/env python
'''
File        :   application.py
Author      :   Akira Nair
Contact     :   akira_nair@brown.edu
Description :   Analysis of TRS identity in coronaviruses
'''

import kmp
import matplotlib.pyplot as plt
import numpy as np

# patterns
patterns = {
    "GROUP_1" :  "CTAAAC",
    "GROUP_2_A" : "TCTAAAC",
    "GROUP_2_B" : "ACGAAC",
    "GROUP_3" : "CTTAACAA"
}

# read files
_, mers = kmp.read_file("data/mers.txt")
_, sars = kmp.read_file("data/sars-cov.txt")
_, sars2 = kmp.read_file("data/sars-cov-2.txt")
texts = {
    "MERS" : mers,
    "SARS-COV" : sars,
    "SARS-COV-2" : sars2
}

# run KMP
strain = []
group_1 = []
group_2_a = []
group_2_b = []
group_3 = []

for text in texts:
    strain.append(text)
    for pattern in patterns:
        print(f"Searching pattern {pattern} in {text}")
        matches = kmp.kmp(patterns[pattern], texts[text])
        n_matches = len(matches)
        len_text = len(texts[text])

        freq = round(n_matches/len_text * 1000, 2)
        freq = round(n_matches)
        print(f"{n_matches} were found. Freq: {freq}")
        if pattern == "GROUP_1":
            group_1.append(freq)
        elif pattern == "GROUP_2_A":
            group_2_a.append(freq)
        elif pattern == "GROUP_2_B":
            group_2_b.append(freq)
        else:
            group_3.append(freq)

# plot results (code referenced from matplotlib docs)
x = np.arange(len(strain))  # the label locations
width = 0.2  # the width of the bars
fig, ax = plt.subplots()
# multiple bar plot
rects1 = ax.bar(x - 0.3, group_1, width, label='GROUP 1')
rects2 = ax.bar(x - 0.1, group_2_a, width, label='GROUP 2 (Heptameric)')
rects3 = ax.bar(x + 0.1, group_2_b, width, label='GROUP 2 (Hexamer)')
rects4 = ax.bar(x + 0.3, group_3, width, label='GROUP 3')
ax.set_ylabel('Matches per KB')
ax.set_xlabel('Strain')
ax.set_title('Number of matches of CS motifs for different coronavirus strains')
# set three ticks
ax.set_xticks([0, 1, 2])
# add coronavirus strain labels
ax.set_xticklabels(strain)
# add legend and labels
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)
# plt.show()
plt.savefig("matches.png", dpi = 200)
