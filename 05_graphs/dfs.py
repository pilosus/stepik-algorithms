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
    #u, v = [int(i) for i in input().split()]
    return reorganize(V) #, u, v

def reorganize(G):
    """Reorganize graph into adjacency-list"""
    for k in G:
        for v in G[k]:
            if (k not in G[v]):
                G[v].append(k)
    return G

# https://www.udacity.com/course/viewer#!/c-cs215/l-48723544/m-48698601
def explore(G, color, cc, ccnum, u):
    cc[u] = ccnum
    color[u] = "Gray" # indicates a back edge!
    for v in G[u]:
        if (color[v] == "White"):
            null = explore(G, color, cc, ccnum, v) ###
    color[u] = "Black"
    return ccnum ###

def DFS(G):
    cc = {}
    ccnum = 0
    color = {}
    for u in G.keys():
        color[u] = "White"
    for u in G.keys():
        if (color[u] == "White"):
            # эксплор обходит все соседние узлы из данного
            ccnum =explore(G, color, cc, ccnum, u)
            ccnum += 1
        #ccnum = cc[u] + 1
    return cc, ccnum

def launch_old():
    G = read()
    cc, ccnum = DFS(G)
    res = set(cc.values())
    if (len(res) == 0):
        print(0)
    else:
        print(max(res))

def launch():
    G = read()
    cc, ccnum = DFS(G)
    print(ccnum)

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
