#!/usr/local/bin/python3

import cProfile
import math

from itertools import islice, count, tee, chain

def siftdown(heap, startpos, pos):
    """pos is an index of the element that violates min-heap property.
    startpos is an index from which the heap is correct downwards.
    """
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    siftdown(heap, startpos, pos)

def insert(heap, item):
    heap.append(item)
    siftdown(heap, 0, len(heap) - 1)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        siftup(heap, 0)
    else:
        returnitem = lastelt
    return returnitem

def heappushpop(heap, item):
    """Fast version of a heappush followed by a heappop."""
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        siftup(heap, 0)
    return item

def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        siftup(x, i)

def find_max(heap):
    maximum = -int(10e9)
    maximum_index = 0
    l = len(heap)
    for i in range((l // 2), l):
        if (heap[i] > maximum):
            maximum = heap[i]
            maximum_index = i
    return maximum_index, maximum
            
def extract(heap, val, i):
    if (i == (len(heap) - 1)):
        temp = heap.pop(i)
    else:
        # swap val with the last element
        heap[i] = heap[-1]
        temp = heap.pop(-1)
        # if the last element less than the element to be extracted, siftup
        # otherwise it's equal and then we do not need to restore the heap
        if (heap[i] < val):
            siftup(heap, i)
    return val

def extract_max_old(heap):
    if (len(heap) < 1):
        return False # Heap underflow
    maximum = max(heap)
    maximum_index = heap.index(maximum)
    if (maximum_index == (len(heap) - 1)):
        maximum = heap.pop(maximum_index)
    else:
        heap[maximum_index] = heap[-1]
        temp = heap.pop(-1)
        siftdown(heap, 0, maximum_index)
    return maximum

def heap():
    n = int(input())
    h = [] # h = [4, 18, 7, 20, 21, 18, 42, 53, 22]
    while (n > 0):
        op = input().split()
        if (op[0] == 'Insert'):
            insert(h, int(op[1]))
        else:
            idx, maximum = find_max(h)
            print(extract(h, maximum, idx))
        #print("Heap: ", h) # debug
        n -= 1

#heap()
cProfile.run('heap()')

#output = []
#while (n > 0):
#    op = input().split()
#    # Insert operator
#    if (op[0] == 'Insert'):
#        insert(h, int(op[1]))
#    # Extract max operator
#    else:
#        output.append(extract_max(h))
#    n -= 1
#
#print("\n".join(map(str, output)))
