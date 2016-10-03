#!/usr/local/bin/python3

import sys
import heapq
import cProfile

########## Comon heap functions  ##########

def parent(i):
    """Return a parent of the ith element of the binary heap"""
    return (i - 1) // 2

def left(i):
    """Return a left child of the ith element of the binary heap """
    return 2 * (i + 1) - 1

def right(i):
    """Return a right child of the ith element of the binary heap"""
    return 2 * (i + 1)

def swap(heap, i, j):
    """Swap two element with the indexes i and j"""
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp

def heap_size(heap):
    return len(heap)

########## Max-Heap ##########

def max_heapify(heap, i):
    l = left(i)
    r = right(i)
    if ((l < len(heap)) and (heap[l] > heap[i])):
        largest = l
    else:
        largest = i
    if ((r < len(heap)) and (heap[r] > heap[largest])):
        largest = r
    if (largest != i):
        swap(heap, i, largest)
        max_heapify(heap, largest)

def build_maxheap(array):
    for i in range((len(array) // 2 - 1), -1, -1):
        max_heapify(array, i)

def maxheap_max(heap):
    return heap[0]

def maxheap_extract_max(heap):
    if (len(heap) < 1):
        return False
    maximum = heap[0]
    heap[0] = heap[-1]
    temp = heap.pop(-1)
    max_heapify(heap, 0)
    return maximum

def maxheap_increase(heap, i, val):
    if (val < heap[i]):
        return False # new value is smaller than current value
    heap[i] = val
    while ((i > 0) and (heap[parent(i)] < heap[i])):
        swap(heap, i, parent(i))
        i = parent(i)

def maxheap_insert(heap, val):
    heap.append(val)
    maxheap_increase(heap, (len(heap) - 1), val)

def maxheapsort(array):
    B = []
    build_maxheap(array)
    for i in range(len(array) - 1, -1, -1):
        swap(array, 0, i)
        B.insert(0, array.pop(-1))
        max_heapify(array, 0)
    return B
        
    
########## Launch  ##########

def maxheap():
    n = int(input()) # to /dev/null
    A = [int(i) for i in input().split()]
    print(" ".join(str(x) for x in maxheapsort(A)))


########## Helper functions ##########
def usage():
    print("usage: heap heaptype test")
    print("heaptype - [max/min/lib]")
    print("test - [true/false]")

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 2):
        usage()
    else:
        if (args[0] == "max"):
            if (args[1] == "true"):
                cProfile.run('maxheap()')
            else:
                maxheap()
