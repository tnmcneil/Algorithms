# CS 330
# Subset Sum Project
# Python 2.7

import random
import math
import heapq
import copy
import matplotlib.pyplot as plt

# 1: Karmarkar Karp

# repeatedly takes the 2 largest numbers  in A and replace the larger of
# the 2 with their difference and the smaller of the 2 with 0
# stop when there is only one non-zero element left and this is an achievable
# residue (can prove using a bipartite graph mapping)

def heapify(A):
            for i in range(len(A)):
                        A[i] = -A[i]

            heap = heapq.heapify(A)
            return A

def push(heap, num):
            heapq.heappush(heap, -num)

def pop(heap):
            return -heapq.heappop(heap)

def KK(A):
            A2 = copy.deepcopy(A)
            heapify(A2)
            i = pop(A2)
            j = pop(A2)
            while j!= 0:
                        diff = i-j
                        push(A2, diff)
                        push(A2, 0)
                        i = pop(A2)
                        j = pop(A2)
            return i

# 2: Repeated Random

# generate k random solutions and return one with the smallest residue

# returns the residue from the input sequences of numbers and signs
def residue(A, S):
            residue = 0
            for i in range(0, len(A)):
                        residue += (A[i]*S[i])
            return abs(residue)

# returns a random sequence 1s and -1s of length x
def R(x):
            return [random.choice([-1,1]) for i in range(x)]

# generates k random sequences and returns the minimum residue
def RR(A):
            x = len(A)
            k = 25000
            residues = [-1 for x in range(k)]
            for i in range(k):
                        residues[i] = residue(A, R(x))
            return min(residues)

# 3: Gradient Descent

# generate an initial random solution and for each k iteration consider
# a random move to a neighbor (defined as a sequence that differs by at most
# 2 signs) and replace with the neighbor if the residue is smaller

# returns a neighbor of S
def RandomMove(S1):
            S = copy.deepcopy(S1)
            i = random.randint(0, len(S)-1)
            j = random.randint(0, len(S)-2)
            if j >= i:
                        j += 1
            S[i] = -S[i]
            chance = random.uniform(0,1)
            if chance > .5:
                        S[j] = -S[j]
            return S

# first generates a random S and then generates k neighbors of S,
# replacing S with its neighbor if its residue is smaller
def GD(A):
            k = 25000
            S = R(len(A))
            while k > 0:
                        neighbor = RandomMove(S)
                        if residue(A, neighbor) < residue(A, S):
                                    S = neighbor
                        k -= 1
            return residue(A, S)

# 4: Simulated Annealing

# first generates a random S and then generates k neighbors of S,
# always replacing S with its neighbor if its residue is smaller, and
# if bigger replace S with its neighbor with a certain probability based on
# the cooling schedule defined in the assighment and return the smallest
# residue over all

def SA(A):
            k = 25000
            residues = [-1 for x in range(k)]
            S = R(len(A))
            residues[0] = residue(A, S)
            count = 1
            while count < k:
                        neighbor = RandomMove(S)
                        if residue(A, neighbor) < residue(A, S):
                                    S = neighbor
                                    residues[count] = residue(A, S)
                        else:
                                    chance = random.uniform(0,1)
                                    power = -(residue(A, neighbor) - residue(A, S))/(pow(10,10)*pow(0.8, (count/300)))
                                    prob = math.exp(power)
                                    if chance < prob:
                                                S = neighbor
                                                residues[count] = residue(A, S)
                                    else:
                                        residues[count] = residue(A, S)
                        count += 1
            return min(residues)
                                    
# testing

# generate 50 random instances of sets of 100 integers chosen uniformly from
# [1, 10^12] and run each approach on these test cases

def randTest():
            k = 25,000
            j = 50
            r = pow(10, 12)
            KKvals = [0]*j
            RRvals = [0]*j
            GDvals = [0]*j
            SAvals = [0]*j
            for i in range(j):
                randList = [random.randint(1, r) for x in range(100)]
                KKvals[i] = KK(randList)
                RRvals[i] = RR(randList)
                GDvals[i] = GD(randList)
                SAvals[i] = SA(randList)

            print("--------")
            print(KKvals)
            print("--------")
            print(RRvals)
            print("--------")
            print(GDvals)
            print("--------")
            print(SAvals)
            print("--------")

# In order to avoid re-running the test every time, here are the saved results
# and used them to generate the plots below
def graph():
            
            KKvals = [63222, 1390572, 113103, 533032, 113494, 7687, 88421, 30024, 12562, 112832, 384677, 3303379, 2012, 115325, 33396, 138398, 142122, 318968, 88876, 262856, 60125, 9404, 233142, 478353, 140509, 136815, 194435, 707680, 763562, 287435, 12054, 9944, 454131, 10902, 10459, 285965, 38497, 269355, 140232, 267577, 459358, 94727, 10804, 60030, 541535, 109978, 739138, 325925, 1463267, 153112]
            RRvals = [333508720, 437458364, 106594707, 183274920, 141694318, 209966771, 52155497, 97226230, 304228924, 199035118, 304540009, 534935403, 205609784, 137127417, 11286992, 223033364, 233596654, 427616212, 152530154, 229493296, 1808609, 12590166, 90730484, 71065085, 43395353, 331365423, 169238457, 149279278, 3623572, 7424471, 3043812, 276090628, 360032077, 415408260, 43301467, 4386371, 211050197, 280478505, 129669528, 301466863, 995692590, 231219871, 403032530, 583824214, 328508987, 501973130, 69226722, 59373213, 95905195, 246853476]
            GDvals = [48556012, 35238174, 123271083, 113417826, 31379708, 182310859, 31610865, 221703620, 679779998, 17466804, 145406079, 38902871, 4734202, 129232447, 572695712, 291957924, 76150414, 245974724, 368881226, 105701696, 277870323, 23433540, 331055244, 970905479, 277819077, 546160291, 12754853, 402801898, 724176580, 196967429, 216011664, 634041534, 105035017, 55592378, 337422555, 559404557, 253844307, 741535949, 819958546, 846025375, 961684006, 10041023, 101199376, 241725006, 743494777, 473861100, 109799808, 38310925, 317751699, 872463758]
            SAvals = [75484364, 101005454, 40280623, 168676894, 418118412, 277167633, 405027213, 193506096, 200808164, 799702674, 434386973, 226108785, 127977250, 190610849, 57079020, 138084404, 6057704, 188976058, 1091045964, 179889674, 870603775, 455671144, 246510992, 234051235, 23950045, 122657927, 116383193, 202015120, 83663742, 248477599, 1262696194, 615595768, 296787153, 114642792, 122387367, 9788229, 376420713, 441012895, 24398276, 587174081, 258881558, 933911223, 8031720, 862013196, 14093875, 1151546082, 16191698, 15809821, 73647639, 165728312]
    
            Xvals = [0]*50
            for i in range(50):
                        Xvals[i] = i+1

            plt.title("Problem 4 KK")
            plt.plot(Xvals, KKvals, c='r', label='KK RESULTS')
            plt.xlabel("Trial Number")
            plt.ylabel("Residues Based on Approaches")
            plt.legend()
            plt.show()

            plt.plot(Xvals, KKvals, c='r', label='KK RESULTS')
            plt.plot(Xvals, RRvals, c='g', label='RR RESULTS')
            plt.plot(Xvals, GDvals, c='b', label='GD RESULTS')
            plt.plot(Xvals, SAvals, c='y', label='SA RESULTS')
            plt.title("Problem 4")
            plt.xlabel("Trial Number")
            plt.ylabel("Residues Based on Approaches")
            plt.legend()
            plt.show()

def main():
            graph()

if __name__ == '__main__':
            main()
