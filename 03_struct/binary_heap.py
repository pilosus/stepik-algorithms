#!/usr/local/bin/python3

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * (i + 1) - 1

def right(i):
    return 2 * (i + 1)

def siftup(heap):
    """heap[-1] is the element to siftup"""
    i = len(heap) - 1
    p = parent(i)
    while (heap[i] < heap[p]):
        temp = heap[p]
        heap[p] = heap[i]
        heap[i] = temp
        i = p
        p = parent(i)
        if (p < 0):
            break

def siftdown(heap, i):
    """Sift down ith element of the heap, 
    that assumed to be violating min-heap property
    """
    l = left(i)
    r = right(i)
    if ((l < len(heap)) and (heap[l] < heap[i])):
        smallest = l
    else:
        smallest = i
    if ((r < len(heap)) and (heap[r] < heap[smallest])):
        smallest = r
    if (smallest != i):
        temp = heap[smallest]
        heap[smallest] = heap[i]
        heap[i] = temp
        siftdown(heap, smallest)
   

def siftdown_orig(heap):
    """heap[0] is the element to siftdown
    """
    leaf_index = 0
    leaf = heap[leaf_index]
    if (len(heap) == 1):
        pass
    elif (len(heap) == 2):
        if (leaf > heap[-1]):
            heap[0] = heap[-1]
            heap[-1] = leaf
        else:
            pass
    else:
        left_child_index = 2 * (leaf_index + 1) - 1
        left_child = heap[left_child_index]
        right_child_index = 2 * (leaf_index + 1)
        right_child = heap[right_child_index]
        if (right_child < left_child):
            current_index = right_child_index
            current = right_child
        else:
            current_index = left_child_index
            current = left_child
        while(leaf > current):
            heap[current_index] = leaf
            heap[leaf_index] = current
            leaf_index = current_index
            leaf = heap[leaf_index]
            left_child_index = False
            right_child_index = False
            if ((2 * (leaf_index + 1) - 1) < len(heap)):
                left_child_index = 2 * (leaf_index + 1) - 1
                left_child = heap[left_child_index]
            if ((2 * (leaf_index + 1)) < len(heap)):
                right_child_index = 2 * (leaf_index + 1)
                right_child = heap[right_child_index]
            if (left_child_index and right_child_index):
                if (right_child < left_child):
                    current_index = right_child_index
                    current = right_child
                else:
                    current_index = left_child_index
                    current = left_child
            elif (left_child_index and not right_child_index):
                current_index = left_child_index
                current = left_child
            elif (not left_child_index and right_child_index):
                current_index = right_child_index
                current = right_child
            else:
                break

            
def insert(heap, val):
    heap.append(val)
    if (len(heap) > 1):
        siftup(heap)

def extract_max(heap):
    maximum = max(heap)
    maximum_index = heap.index(maximum)
    if (maximum_index == (len(heap) - 1)):
        maximum = heap.pop(maximum_index)
    else:
        heap[maximum_index] = heap[-1]
        temp = heap.pop(-1)
        siftdown(heap, maximum_index)
    return maximum

n = int(input())
h = []
output = []

#while (n > 0):
#    op = input().split()
#    # Insert operator
#    if (op[0] == 'Insert'):
#        insert(h, int(op[1]))
#    # Extract operator
#    else:
#        output.append(extract_max(h))
#    n -= 1
#
#print("\n".join(map(str, output)))

while (n > 0):
    op = input().split()
    # Insert operator
    if (op[0] == 'Insert'):
        insert(h, int(op[1]))
    # Extract max operator
    else:
        print(extract_max(h))
    n -= 1
