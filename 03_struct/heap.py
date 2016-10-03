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

########## Min-Heap ##########

def minheap_siftdown(heap, i):
    """Sift down the ith element of the heap, 
    that assumed to be violating min-heap property, 
    i.e. heap[i] > heap[left(i)] or heap[i] > heap[right(i)]
    """
    l = left(i)
    r = right(i)
    if ((l < heap_size(heap)) and (heap[l] < heap[i])):
        smallest = l
    else:
        smallest = i
    if ((r < heap_size(heap)) and (heap[r] < heap[smallest])):
        smallest = r
    if (smallest != i):
        swap(heap, i, smallest)
        minheap_siftdown(heap, smallest)

def build_minheap(array):
    """Build a min-heap"""
    for i in range((heap_size(array) // 2), -1, -1):
        minheap_siftdown(array, i)
  
def minheap_siftup(heap, i):
    """Sift up the ith element of the heap,
    that assumed to be violating min-heap property"""
    p = parent(i)
    if ((p >= 0) and (heap[p] > heap[i])):
        largest = p
    else:
        largest = i
    if (largest != i):
        swap(heap, i, largest)
        minheap_siftup(heap, largest)

def minheap_extract_min(heap):
    """Extract minimum element of the heap"""
    if (heap_size(heap) < 1):
        return False # Heap underflow
    minimum = heap[0]
    heap[0] = heap[-1]
    temp = heap.pop(-1)
    minheap_siftdown(heap, 0)
    return minimum

def minheap_find_max(heap):
    maximum = -int(10e9)
    maximum_index = 0
    l = len(heap)
    for i in range((l // 2), l):
        if (heap[i] > maximum):
            maximum = heap[i]
            maximum_index = i
    return maximum_index, maximum

def minheap_find_max2(heap):
    l = len(heap)
    end = -(l // 2 + 1)
    startpos = l + end
    maximum = max(heap[end:])
    end_index = heap[end:].index(maximum)
    maximum_index = startpos + end_index
    return maximum_index, maximum
            
def minheap_extract(heap, val, i):
    if (i == (len(heap) - 1)):
        temp = heap.pop(i)
    else:
        # swap val with the last element
        heap[i] = heap[-1]
        temp = heap.pop(-1)
        # if the last element less than the element to be extracted, siftup
        # otherwise it's equal and then we do not need to restore the heap
        if (heap[i] < val):
            minheap_siftup(heap, i)
    return val

def minheap_extract_max(heap):
    """Extract minimum element of the heap"""
    if (heap_size(heap) < 1):
        return False # Heap underflow
    idx, maximum = minheap_find_max2(heap)
    return minheap_extract(heap, maximum, idx)


def minheap_insert(heap, val):
    """Insert value into the heap"""
    heap.append(val)
    minheap_siftup(heap, (heap_size(heap) - 1))

def minheap_heap_min(heap):
    return heap[0]

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

########## Libheap ##########

    
########## Launch  ##########

def minheap():
    n = int(input())
    h = [] # h = [4, 18, 7, 20, 21, 18, 42, 53, 22]
    while (n > 0):
        op = input().split()
        if (op[0] == 'Insert'):
            minheap_insert(h, int(op[1]))
        else:
            print(minheap_extract_max(h))
        #print("Heap: ", h) # debug
        n -= 1

def maxheap():
    n = int(input())
    h = [] # h = [4, 18, 7, 20, 21, 18, 42, 53, 22]
    while (n > 0):
        op = input().split()
        if (op[0] == 'Insert'):
            maxheap_insert(h, int(op[1]))
        else:
            print(maxheap_extract_max(h))
        #print("Heap: ", h) # debug
        n -= 1

def libheap():
    n = int(input())
    h = [] # h = [4, 18, 7, 20, 21, 18, 42, 53, 22]
    while (n > 0):
        op = input().split()
        if (op[0] == 'Insert'):
            maxheap_insert(h, int(op[1]))
        else:
            print(maxheap_extract_max(h))
        #print("Heap: ", h) # debug
        n -= 1

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
        elif (args[0] == "min"):
            if (args[1] == "true"):
                cProfile.run('minheap()')
            else:
                minheap()
        else:
            # lib
            if (args[1] == "true"):
                cProfile.run('libheap()')
            else:
                libheap()

