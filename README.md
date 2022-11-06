# KMP Algorithm and DFA Pattern Recognizer
> Akira Nair, Brown University,  CSCI 1810 Project 2
### Usage:
To pattern match using KMP, run `sh kmp.sh $filepath` and specify the location of a text file that contains the text on its first line and the pattern on its second line. The output will be the index of the matches found in the string.

To create a DFA that recognizes a particular pattern, run `sh dfa.sh $input $output`. Input is the location of a text file containing the pattern that the DFA must recognize and output is the location of an output .dot file that represents the DFA. The .dot file can be used by a DFA visualization tool such as [Graphviz](https://dreampuf.github.io/GraphvizOnline/).

### Bugs and Notes:
The DFA only recognizes the DNA nucleotide alphabet [A, C, G, T]. If other symbols are used in the pattern, the DFA will no longer be valid. No known bugs have been found. 

