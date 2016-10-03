#!/usr/local/bin/python3

# A = [2, 8, 7, 1, 3, 5, 6, 4]
# D = [(0, 5), (7, 10), (1, 3), (1, 4), (3, 8)]
# E = {}
# for i,j in enumerate(D):
#     E[i] = j
# {0: (0, 5), 1: (7, 10), 2: (1, 3), 3: (1, 4), 4: (3, 8)}  
# sorted(D, key=lambda point: point[0]) 
# P = [2, 4, 8, 11]

import cProfile
import sys
from random import randint
from math import log, ceil, floor
import heapq

############################## Heapsort ##############################
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

############################## Quicksort ##############################

### Partition 

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, l, r):
    x = A[l]
    i = l
    j = i
    for i in range((l + 1), (r + 1)):
        if A[i] <= x:
            j += 1
            swap(A, j, i)
    swap(A, l, j)
    return j

def randomized_partition(A, l, r):
    i = randint(l, r)
    swap(A, r, i)
    return partition(A, l, r)

def median_partition(A, l, r):
    if ((r - l) >= 3):
        m = []
        for i in range(3):
            m.append(randint(l, r))
        m.sort()
        i = m[1] # median of 3
        swap(A, r, i)
        return partition(A, l, r)
    else:
        i = randint(l, r)
        swap(A, r, i)
        return partition(A, l, r)

def last_partition(A, l, r):
    """Pivot is the last element"""
    x = A[r]
    i = l - 1
    j = l
    #for j in range(l, r - 1):
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            #swap(A, j, i)
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    #swap(A, i + 1, r)
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1


### Sort

def quicksort(A, l, r):
    while l < r:
        m = partition(A, l, r)
        quicksort(A, l, m - 1)
        l = m + 1

def randomized_quicksort(A, l, r):
    while l < r:
        m = randomized_partition(A, l, r)
        randomized_quicksort(A, l, m - 1)
        l = m + 1

def quicksort3(A, l, r):
    while l < r:
        m = median_partition(A, l, r)
        quicksort3(A, l, m - 1)
        l = m + 1

def introsort(A, l, r):
    c = 2
    max_recur_num = c * ceil(log(len(A), 2))
    recur_count = 0
    while l < r:
        m = randomized_partition(A, l, r)
        randomized_quicksort(A, l, m - 1)
        l = m + 1

############################## Launch ##############################

def read():
    n, m = [int(i) for i in input().split()]
    S = []
    while (n >= 1): # segments coordinates
       s, e = [int(i) for i in input().split()]
       S.append([s, e])
       n -= 1
    P = [int(i) for i in input().split()] # points coordinates
    return S, P


def count_segments(S, p):
    """Count how many segments the pooint p lays on.
    """
    c = 0
    counter = 0
    while (c < len(S)):
        if (S[c][0] <= p):
            if (S[c][1] >= p):
                counter += 1
            else:
                c += 1
                continue
        else:
            break
        c += 1
    return counter
           
def quick():
    S, P = read()
    quicksort(S, 0, len(S) - 1)
    result = []
    for p in P:
        result.append(count_segments(S, p))
    print(" ".join(str(x) for x in result))

def randquick():
    S, P = read()
    randomized_quicksort(S, 0, len(S) - 1)
    result = []
    for p in P:
        result.append(count_segments(S, p))
    print(" ".join(str(x) for x in result))

def quick3():
    S, P = read()
    quicksort3(S, 0, len(S) - 1)
    result = []
    for p in P:
        result.append(count_segments(S, p))
    print(" ".join(str(x) for x in result))

def timsort():
    S, P = read()
    result = []
    for p in P:
        result.append(count_segments(S, p))
    print(" ".join(str(x) for x in result))

def naive2():
    S, P = read()
    S.sort()
    result = []
    for p in P:
        print(str(count_segments(S, p)), end=' ')

###

def naive():
    S, P = read()
    S.sort()
    ls = []
    rs = []
    for i in range(len(S)):
        ls.append(S[i][0])
        rs.append(S[i][1])

    inf = 50001
    ls.append(inf)
    rs.append(inf)

    for p in P:
        new_ls = list(ls)
        #new_ls.append(p)
        new_ls[-1] = p ### new
        idx = last_partition(new_ls, 0, len(new_ls) - 1)
        ##print("\n" + "### " + str(idx) + " ###" + "\n") ### debug
        if (idx == 0):
            print(str(0), end=' ')
            continue
        counter = idx
        for i in range(idx):
            if rs[i] < p:
                counter -= 1
        print(str(counter), end=' ')
        
###


def usage():
    print("usage: quicksort algtype launchtype")
    print("algtype - [quick/randquick/quick3/naive]")
    print("launchtype - [profiler/plain]")


if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) == 0):
        usage()
    else:
        if (args[0] == "quick"):
            if (args[1] == "profiler"):
                cProfile.run('quick()')
            else:
                quick()
        elif (args[0] == "randquick"):
            if (args[1] == "profiler"):
                cProfile.run('randquick()')
            else:
                randquick()
        elif (args[0] == "quick3"):
            if (args[1] == "profiler"):
                cProfile.run('quick3()')
            else:
                quick3()
        else:
            if (args[1] == "profiler"):
                cProfile.run('naive()')
            else:
                naive()
