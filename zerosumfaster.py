# Theresa McNeil
# U09757615
# CS 330 Assignment 1
# 4 b: zerosortfaster.py in O(n^2) time
# Python 3.6.4

def zerosumfaster(sequence):

            # create an empty dictionary
            
            pairs = {}

            # fill the dictionary with the indices and integers from the
            # input list, essentially "hashing" each duplicate integer
            # to the same location; runs in O(n) time
            
            for a in range(0, len(sequence)):
                        pairs[sequence[a]] = a

            # again iterate over the sequence in a double nested for loop
            # running in O(n^2) time to calculate all possible sums of pairs
            
            for i in range(0, len(sequence) - 2):
                        for j in range(i + 1, len(sequence) - 1):

                                    # let x again be the third element needed to
                                    # complete the zero sum which is the negation
                                    # of the pair calculated
                                    
                                    x = 0 - (sequence[i] + sequence[j])

                                    # next must check to see if x is in the dictionary
                                    # which means we have a solution
                                    # lookup in the dictionary runs in O(1) time
                                    
                                    if x in pairs:
                                                print("Success!", sequence[i], sequence[j], x)
                                                return i, j, sequence.index(x)
                                    else:
                                                return "No"

"""
This program works because it calculates the sum all possible pairs of integers and then
negates that sum to find the third integer necessary to sum the three to zero.  The double
nested for loop again runs in O(n^2) time but because the lookup has been reduced to O(1) time
the total run time is now O(n) + O(n^2) = O(n^2).  It must terminate because it stops searching
the input sequence before the last digit because at that point if there was a triplet it would
have been found.
"""
