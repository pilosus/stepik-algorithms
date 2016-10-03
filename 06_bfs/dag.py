#!/usr/local/bin/python3

import sys
import cProfile
from heapq import heappush, heappop, heapify

sys.setrecursionlimit(20000) # max depth recursion

#################### Read

def read():
    n, m, s = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    w = {}
    S = {}
    while (m >= 1):
       key, val, weight = [int(i) for i in input().split()]
       if (weight < 0):
           S[weight] = key
       if (val not in V[key]):
           V[key].append(val)
       if ((key, val) in w):
           if (w[(key, val)] > weight):
               w[(key, val)] = weight
       else:
           w[(key, val)] = weight
       m -= 1
    return V, w, s, S

#################### Toposort

def topoexplore(G, time, color, pred, discovered, finished, res, u):
    time = time + 1
    discovered[u] = time
    color[u] = "Gray" # indicates a back edge!
    for v in G[u]:
        if (color[v] == "White"):
            pred[v] = u
            topoexplore(G, time, color, pred, discovered, finished, res, v)
        if (color[v] == "Gray"):
            return 1, u # there is a cycle on the way from u
    color[u] = "Black"
    res.insert(0, u)
    time = time + 1
    finished[u] = time
    return 0, u

def toposort(G):
    """Topologically sort a DAG."""
    cycles = []
    res = []
    time = 0
    color = {}
    pred = {} # predecessor
    discovered = {} # time of discovery
    finished = {} # finish time
    for u in G.keys():
        color[u] = "White"
        pred[u] = None
        discovered[u] = None ### vrs
        finished[u] = None ### vrs
    time = 0
    for u in G.keys():
        if (color[u] == "White"):
            cycle_exists, u = topoexplore(G, time, color, pred, discovered, finished, res, u)
            if (cycle_exists):
                cycles.append(u)
    return res, cycle_exists, cycles

#################### Dijkstra

class PriorityDict(dict):
    def __init__(self, *args, **kwargs):
        super(PriorityDict, self).__init__(*args, **kwargs)
        self._rebuild_heap()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.items()]
        heapify(self._heap)

    def empty(self):
        return len(self) == 0

    def smallest(self):
        heap = self._heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heappop(heap)
            v, k = heap[0]
        return k

    def pop_smallest(self):
        heap = self._heap
        v, k = heappop(heap)
        while k not in self or self[k] != v:
            v, k = heappop(heap)
        del self[k]
        return k

    def __setitem__(self, key, val):
        super(PriorityDict, self).__setitem__(key, val)
        
        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (val, key))
        else:
            self._rebuild_heap()

    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
            return val
        return self[key]

    def update(self, *args, **kwargs):
        super(PriorityDict, self).update(*args, **kwargs)
        self._rebuild_heap()

    def sorted_iter(self):
        while self:
            yield self.pop_smallest()


def dijkstra(G, w, s):
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

def dijkstra_shortest_path(G, w, s, v):
    dist, pred = dijkstra(G, w, s)
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

#################### Bellman Ford

def bf(G, w, s):
    """Return 1 if there is a negative cycle in the graph.
    Otherwise return 0 as well as shortest paths and their weights.
    """
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int

    for u in G.keys():
        dist[u] = INF
        pred[u] = None

    dist[s] = 0

    for i in range(len(G.keys()) - 1):
        for (u, v) in w.keys():
            if (dist[v] > dist[u] + w[(u, v)]):
                dist[v] = dist[u] + w[(u, v)]
                pred[v] = u
    
    for (u, v) in w.keys():
        if (dist[v] > dist[u] + w[(u, v)]):
            dist[v] = -INF
            pred[v] = u
            res = 1
            #return 1, dist, pred
        else:
            res = 0

    return res, dist, pred
    #return 0, dist, pred

def bf_shortest_path(G, w, pred, s, v):
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

#################### DAG Shortest Path

def dag_shortest_paths(G, w, s):
    """Find the shortest path in a directed acyclic graph.
    """
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int

    for u in G.keys():
        dist[u] = INF
        pred[u] = None

    dist[s] = 0

    GS, cycle_exists, cycles = toposort(G)
    
    for u in GS:
        for v in G[u]:
            if (dist[v] > dist[u] + w[(u, v)]):
                dist[v] = dist[u] + w[(u, v)]
                pred[v] = u

    return dist, pred
    
def dag_count(G, w, pred, s, v):
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

#################### Non shortest path

#################### Launch
def launch():
    G, w, s, S = read()
    INF = float("inf") # infinity, > than any int

    # Есть ли в графе циклы?
    GS, cycle_exists, cycles = toposort(G)

    # Если граф ацикличный, находим кратчайшие пути до всех вершин из s
    if (not cycle_exists):
        dist, pred = dag_shortest_paths(G, w, s)
        for v in G.keys():
            print(dag_count(G, w, pred, s, v))
    # Если граф имеет циклы, проверяем, являются ли они отрицательнымми
    else:
        negcycle, dist, pred = bf(G, w, s)
        # Если неотрицательные, 
        # то можем находить кратчайшие пути до всех вершин через BF
        if (not negcycle):
            for v in G.keys():
                print(bf_shortest_path(G, w, pred, s, v))
        else:
        # Если есть отрицательные циклы
            for v in G.keys():
                if (dist[v] == INF):
                    print("*")
                elif (dist[v] == -INF):
                    print("-")
                else:
                    print(str(dist[v]))

def usage():
    print("usage: dag.py launchtype")
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

