"""
Solves the problem of finding 2 indexes i,j in a list L = [1..N] such that sum(L[i:j]) is maximal.
It does this in O(n*log(n)) time complexity.
The method is divide and conquer, shrinking the search space by 1 element
each iteration gives log(n) recursive calls. We simply keep track
of the max sum found and the indexes used.
"""

from math import log
c = 0

def findIndex(L, i, j,shrinkLeft):
    global c
    c += 1
    if len(L) == 1:
        return i, j, L[0]

    maxSum = 0
    for x in L:
        maxSum += x

    if shrinkLeft:
        i_,j_,S_ = findIndex(L[1:], i+1, j,False)
    else:
        i_,j_,S_ = findIndex(L[:-1], i, j-1, True)
    if maxSum < S_:
        return i_,j_,S_
        
    return i,j,maxSum

L = [10,-12,5,7,-2,4,-11]
res = findIndex(L, 0, len(L),True)
print("Result: i={}, j={} gives sum: {}".format(res[0],res[1], res[2]))
print("nlog(n) is: {}, algoritm did: {}".format(len(L)*log(len(L)), c))
