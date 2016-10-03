#!/usr/local/bin/python3

import cProfile
import sys

#sys.setrecursionlimit(20000) # max depth recursion

#####

def read():
    n, m = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    while (m >= 1):
       key, val = [int(i) for i in input().split()]
       V[key].append(val)
       m -= 1
    return V

def isacyclic(G):
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
            res = explore(G, time, color, pred, discovered, finished, u)
            if (res == 1):
                return 1
    return 0

def DFS(G):
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
            res = explore(G, time, color, pred, discovered, finished, u)
            if (res == 1):
                return 1
    return discovered, finished

def explore(G, time, color, pred, discovered, finished, u):
    time = time + 1
    discovered[u] = time
    color[u] = "Gray" # indicates a back edge!
    for v in G[u]:
        if (color[v] == "White"):
            pred[v] = u
            explore(G, time, color, pred, discovered, finished, v)
        ### debug
        if (color[v] == "Gray"):
            return 1
    color[u] = "Black"
    time = time + 1
    finished[u] = time
    return 0

def topoexplore(G, time, color, pred, discovered, finished, res, u):
    time = time + 1
    discovered[u] = time
    color[u] = "Gray" # indicates a back edge!
    for v in G[u]:
        if (color[v] == "White"):
            pred[v] = u
            topoexplore(G, time, color, pred, discovered, finished, res, v)
        if (color[v] == "Gray"):
            return 1 # acyclic
    color[u] = "Black"
    res.insert(0, u)
    time = time + 1
    finished[u] = time
    return 0

def toposort(G):
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
            topoexplore(G, time, color, pred, discovered, finished, res, u)
    return res
    
def launch():
    G = read()
    print(isacyclic(G))
    #print(" ".join(str(x) for x in toposort(G)))
 



############################## Launch ##############################
def usage():
    print("usage: dfs launchtype")
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
