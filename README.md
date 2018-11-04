# Algorithms
Collection of algorithm implementations for my Intro to Algorithms class

Partition Problem:
Given a sequence A of n non negative numbers, output a sequence S of n signs {-1,1} such that the residue is minimized, where the "residue" is the sum from i = 1 to n of A[i]*S[i].  This can also be thought of as partitioning the sequence into 2 subsets such that their sums are as close as possible, and the residue is the difference between them.  
This problem is NP-Complete, however here are 4 heuristic attempts at solving it
This implementation uses 25,000 iterations of each approach on 50 sequences of 100 integers in the range [1, 10^12]
Change k to adjust the number of iterations or r to adjust the range which can both be found in randTest()
graph() saved the results using 25,000 iterations to produce a visual representation of the performance of each approach.

ZeroSumSort & ZeroSum Faster:
2 approaches to finding 3 numbers in a list which sum to 0
