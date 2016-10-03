#!/usr/local/bin/python3

import sys
import cProfile

def read():
    n, m = [int(i) for i in input().split()]
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
    return V, w, S

def bf(G, w, s):
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
            return 1

    return 0

def launch():
    G, w, S = read()
    result = 0
    V = [S[i] for i in sorted(S.keys())]
    for s in V:
        if (bf(G, w, s) == 1):
            result = 1
            break
    print(result)
    #print(bf(G, w, s))

def usage():
    print("usage: bf.py launchtype")
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


"""
def read():
    n, m = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    w = {}
    s = []
    while (m >= 1):
       key, val, weight = [int(i) for i in input().split()]
       if (weight < 0):
           s.append(key)
       V[key].append(val)
       w[(key, val)] = weight
       m -= 1
    return V, w, s

def bf(G, w, s):
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
            return 1

    return 0

def launch():
    G, w, s = read()
    result = 0
    s.sort(reverse=True)
    for i in s:
        if (bf(G, w, i) == 1):
            result = 1
            break
    print(result)

launch()
"""
