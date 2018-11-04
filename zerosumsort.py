# Theresa McNeil
# U09757615
# CS 330 Assignment 1
# 4 a: zerosumsort.py in O(n^2 logn) time
#Python 3.6.4

def zerosumsort(sequence):

            # make a hard copy of the sequence to refer to later to preserve the original indices
            # takes O(n) time

            original = list(sequence)
            
            # sort the input sequence which takes nlog(n) time (given by Python)
            
            sequence.sort()

            # find all pairs of numbers in the sequence using a double nested for loop and compute
            # their sum which takes n^2 time because it iterates through a list of n integers twice
            # calculating the sum takes constant time because of instant lookup

            for i in range (0, len(sequence)):
                        for j in range(i+1, len(sequence)):

                                    x = 0 - (sequence[i] + sequence[j])

                                    # now use binary search (O(logn)) to search the list to see if a value equal
                                    # to x exists because that would imply that sequence[i] + sequence[j]
                                    # + x = 0 and x would be our third integer

                                    start = 0
                                    end = len(sequence) - 1

                                    while start <= end:
                                                k = (start + end) // 2
                                                if ((sequence[k] == x) and k != i and k != j):
                                                            print ("Success!")
                                                            # print ("ints are: ", sequence[i], sequence[j], sequence[k])
                                                            return original.index(sequence[i]), original.index(sequence[j]), original.index(sequence[k])
                                                elif sequence[k] > x:
                                                            end = k - 1
                                                elif sequence[k] < x:
                                                            start = k + 1
                                                else:
                                                            return "No"
                                                
            return "No"
                                    
# this program works by first creating a hard copy of the input sequence of integers to preserve the original indices (takes O(n) time) before sorting the
# input sequence using the built in .sort() function in python which takes O(nlog(n)) time as given by the algorithm. Next it iterates through all possible
# pairs in the a double nested for loop, with each loop running in O(n) time, and takes their sum which takes O(1) time since it uses the indexing of
# the list. Next it uses binary search on the sorted list which we know takes O(log(n)) time.  The binary search is looking for the negative of the sum we
# previously calculated because this would imply the third integer which sums to 0 is in the list, but also must check to make sure its index is not equal
# to either of the other indices so as to prevent the use of duplicates.  If such a match is found we have a success! We then use Python's built in .index
# on the hard copy of the original list to obtain the correct indices of the triplets.  Each lookup takes O(n) times and there are three lookups so
# O(n) + O(n) + O(n) = O(3n) = O(n) however because this occurs in an if statement it is only computed once and therefore is added to the overall O(n), not
# multiplied.  If no such match is found the function returns "No"
# the overall time complexity is O(n) + O(nlogn) + O(n*n*logn + n + n + n) = O(n) + O(nlogn) + O(n^2logn + 3n) = O(n^2logn) beccause this leading term grows to
# infinity much faster than the rest of them
