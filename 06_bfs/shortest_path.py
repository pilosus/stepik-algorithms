#!/usr/local/bin/python3

import cProfile
import sys

def read():
    n, m = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    while (m >= 1):
       key, val = [int(i) for i in input().split()]
       V[key].append(val)
       m -= 1
    u, v = [int(i) for i in input().split()]
    return reorganize(V), u, v

def reorganize(G):
    """Reorganize graph into adjacency-list"""
    for k in G:
        for v in G[k]:
            if (k not in G[v]):
                G[v].append(k)
    return G

def BFS(G, s):
    color = {}
    dist = {}
    pred = {}
    INF = float("inf") # infinity, > than any int
    for u in G.keys():
        color[u] = "White"
        dist[u] = INF
        pred[u] = None
    color[s] = "Gray"
    dist[s] = 0
    pred[s] = None
    Q = [] # FIFO queue
    Q.append(s) # enqueue
    while (len(Q) != 0):
        u = Q.pop(0) # dequeue
        for v in G[u]:
            if (color[v] == "White"):
                color[v] = "Gray"
                dist[v] = dist[u] + 1
                pred[v] = u
                Q.append(v) # enqueue
        color[u] = "Black"
    return dist, pred

def count(G, pred, s, t):
    """Count number of edges between vertices s and t.
    Return -1 if there are no edges.
    """
    if (pred[t] == None):
        return -1
    counter = 0
    current = t
    while (current != s):
        current = pred[current]
        counter += 1
    return counter

def path(G, pred, s, t):
    if (s == t):
        print(s)
    elif (pred[t] == None):
        print("No path from " + str(s) + " to " +  str(t) + " exists")
    else:
        path(G, pred, s, pred[t])
        print(t)

def launch():
    G, s, t = read()
    dist, pred = BFS(G, s)
    print(count(G, pred, s, t))
    

############################## Launch ##############################
def usage():
    print("usage: shortest_path.py launchtype")
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
