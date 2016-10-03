#!/usr/local/bin/python3

import sys
import cProfile
from math import ceil
inv = 0 # global variable

############################## Merge Sort ##############################

def inject(Q, elem):
    Q.append(elem)

def eject(Q):
    result = Q.pop(0)
    return result

def merge(left, right):
    global inv # inversions
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            inv = inv + (len(left) - left_idx)
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result    

def itermergesort(A):
    Q = []
    for i in range(len(A)):
        inject(Q, list([A[i]]))
    while (len(Q) > 1):
        inject(Q, merge(eject(Q), eject(Q)))
    return Q[0] # Q is a list of lists

def mergesort(A):
    if len(A) < 2: 
        return A
    m = len(A) // 2 
    return merge(mergesort(A[:m]), mergesort(A[m:])) 

############################## Launch ##############################
def read():
    n = int(input()) # to /dev/null
    return [int(i) for i in input().split()] # A = [7, 2, 5, 3, 7, 13, 1, 6]

def recurcount():
    A = read()
    mergesort(A)
    print(inv)

def itercount():
    A = read()
    itermergesort(A)
    print(inv) # WRONG ANSWER

def usage():
    print("usage: mergesort algtype launchtype")
    print("algtype - [iter/recur]")
    print("launchtype - [profiler/plain]")

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) == 0):
        usage()
    else:
        if (args[0] == "iter"):
            if (args[1] == "profiler"):
                cProfile.run('itercount()')
            else:
                itercount()
        else:
            if (args[1] == "profiler"):
                cProfile.run('recurcount()')
            else:
                recurcount()
