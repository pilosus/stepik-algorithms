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
    u, v = [int(i) for i in input().split()]
    return reorganize(V), u, v

def reorganize(G):
    """Reorganize graph into adjacency-list"""
    for k in G:
        for v in G[k]:
            if (k not in G[v]):
                G[v].append(k)
    return G
    

def path_exists():
    G, u, v = read()
    visited = {}
    for i in G.keys():
        visited[i] = False
    explore(G, visited, v)
    if (visited[u]):
        print(str(1))
    else:
        print(str(0))

def explore(G, visited, v):
    visited[v] = True
    # перебираем все соседние ребка
    for u in G[v]:
        if (visited[u] == False):
            explore(G, visited, u)

############################## Launch ##############################
def usage():
    print("usage: explore.py launchtype")
    print("launchtype - [profiler/plain]")

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 1):
        usage()
    else:
        if (args[0] == "profiler"):
            cProfile.run('path_exists()')
        else:
            path_exists()
