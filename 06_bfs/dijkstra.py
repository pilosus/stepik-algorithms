#!/usr/local/bin/python3

import cProfile
import sys
from heapq import heappush, heappop, heapify
from queue import PriorityQueue
import itertools

#################### Read

def read():
    n, m = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    w = {}
    while (m >= 1):
       key, val, weight = [int(i) for i in input().split()]
       if (val not in V[key]):
           V[key].append(val)
       if ((key, val) in w):
           if (w[(key, val)] > weight):
               w[(key, val)] = weight
       else:
           w[(key, val)] = weight
       m -= 1
    u, v = [int(i) for i in input().split()]
    return V, w, u, v

#################### Min-Heap

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

def minheap_insert(heap, val):
    """Insert value into the heap"""
    heap.append(val)
    minheap_siftup(heap, (heap_size(heap) - 1))

def decrease_key(heap, x, k):
    """Decrease the value of element x's key to the new value k,
    which assumed to be less as large as x's current key value.
    """
    if (k > heap[x]):
        print("Error: the new key is larger that the current key")
    heap[x] = k
    while ((x > 0) and (heap[parent(x)] > heap[x])):
        swap(heap, x, parent(x))
        x = parent(x)

#################### heapq

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

#################### yet another priority queue
class PriorityDict(dict):
    """Dictionary that can be used as a priority queue.

    Keys of the dictionary are items to be put into the queue, and values
    are their respective priorities. All dictionary methods work as expected.
    The advantage over a standard heapq-based priority queue is
    that priorities of items can be efficiently updated (amortized O(1))
    using code as 'thedict[item] = new_priority.'

    The 'smallest' method can be used to return the object with lowest
    priority, and 'pop_smallest' also removes it.

    The 'sorted_iter' method provides a destructive sorted iterator.
    """
   
    def __init__(self, *args, **kwargs):
        super(PriorityDict, self).__init__(*args, **kwargs)
        self._rebuild_heap()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.items()]
        heapify(self._heap)

    def empty(self):
        return len(self) == 0

    def smallest(self):
        """Return the item with the lowest priority.
        Raises IndexError if the object is empty.
        """
        heap = self._heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heappop(heap)
            v, k = heap[0]
        return k

    def pop_smallest(self):
        """Return the item with the lowest priority and remove it.
        Raises IndexError if the object is empty.
        """
        
        heap = self._heap
        v, k = heappop(heap)
        while k not in self or self[k] != v:
            v, k = heappop(heap)
        del self[k]
        return k

    def __setitem__(self, key, val):
        # We are not going to remove the previous value from the heap,
        # since this would have a cost O(n).
        
        super(PriorityDict, self).__setitem__(key, val)
        
        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (val, key))
        else:
            # When the heap grows larger than 2 * len(self), we rebuild it
            # from scratch to avoid wasting too much memory.
            self._rebuild_heap()

    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
            return val
        return self[key]

    def update(self, *args, **kwargs):
        # Reimplementing dict.update is tricky -- see e.g.
        # http://mail.python.org/pipermail/python-ideas/2007-May/000744.html
        # We just rebuild the heap from scratch after passing to super.
        
        super(PriorityDict, self).update(*args, **kwargs)
        self._rebuild_heap()

    def sorted_iter(self):
        """Sorted iterator of the priority dictionary items.

        Beware: this will destroy elements as they are returned.
        """
        
        while self:
            yield self.pop_smallest()



#################### Dijktra's algorithm
def dijkstra(G, w, s):
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int
    for u in G.keys():
        dist[u] = INF
        pred[u] = None
    dist[s] = 0
    H = [i for i in dist.keys()]
    build_minheap(H)
    while (len(H) != 0):
        u = minheap_extract_min(H)
        for (u, v) in w.keys():
            if (dist[v] > dist[u] + w[(u, v)]):
                dist[v] = dist[u] + w[(u, v)]
                pred[v] = u
                decrease_key(H, H.index(v), dist[v])
    return pred


def dijkstra2(G, w, s):
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int
    for u in G.keys():
        dist[u] = INF
        pred[u] = None
        add_task(v, dist[u])
    dist[s] = 0
    
    #pq = [d for d in dist.keys()]
    #heapify(pq)

    while (len(pq) != 0):
        try:
            u = pop_task()
        except KeyError:
            return dist, pred
        for v in G[u]:
        #for (u, v) in w.keys():
            if (dist[v] > dist[u] + w[(u, v)]):
                dist[v] = dist[u] + w[(u, v)]
                pred[v] = u
                add_task(v, dist[v])
    return dist, pred

def dijkstra3(G, w, s):
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int

    for u in G.keys():
        dist[u] = INF
        pred[u] = None
    dist[s] = 0

    D = {v: dist[v] for v in G.keys()}
    H = PriorityDict(D)
    
    while (not H.empty()):
        u = H.pop_smallest()
        for v in G[u]:
        #for (u, v) in w.keys():
            if (dist[v] > dist[u] + w[(u, v)]):
                dist[v] = dist[u] + w[(u, v)]
                pred[v] = u
                H[v] = dist[v]
    return dist, pred

def shortest(G, w, pred, s, v):
    """Return the shortest path from s to v or -1 if there is no path
    between them.
    """
    if (pred[v] == None):
        return -1
    counter = 0
    current = v
    while (current != s):
        counter += w[(pred[current], current)]
        current = pred[current]
    return counter

def shortestpath(G, w, pred, s, v):
    if (pred[v] == None):
        return -1
    P = []
    while 1:
        P.append(v)
        if (v == s):
            break
        v = pred[v]
    P.reverse()
    counter = 0
    for i in range(len(P) - 1):
        counter += w[(P[i], P[i + 1])]
    return counter


#################### Launch
def launch():
    G, w, s, v = read()
    dist, pred = dijkstra3(G, w, s)
    #print(shortest(G, w, pred, s, v))
    print(shortestpath(G, w, pred, s, v))

############################## Launch ##############################
def usage():
    print("usage: dijkstra.py launchtype")
    print("launchtype - [profiler/plain]")

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 1):
        usage()
    else:
        if (args[0] == "profiler"):
            cProfile.run('launch()')
        else:
            launch()
