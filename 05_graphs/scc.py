#!/usr/local/bin/python3

import cProfile
import sys
import operator

sys.setrecursionlimit(20000) # max depth recursion

#####

def read():
    n, m = [int(i) for i in input().split()]
    V = {i: [] for i in range(1, n + 1)} # graph as a dict
    while (m >= 1):
       key, val = [int(i) for i in input().split()]
       V[key].append(val)
       m -= 1
    return V

def transpose(G):
    V = {i: [] for i in G.keys()}
    for v in G.keys():
        for u in G[v]:
          if (v not in V[u]):
              V[u].append(v)
    return V
    
def DFS_t(G):
    """DFS for a transpose graph"""
    res = []
    scc = {}
    sccnum = 0 # for comapability only
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
            null = explore(G, time, color, pred, discovered, finished, scc, sccnum, res, u)
    return res

def DFS(G, order):
    res = []
    scc = {}
    sccnum = 0
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
    for u in order:
        if (color[u] == "White"):
            sccnum = explore(G, time, color, pred, discovered, finished, scc, sccnum, res, u)
            sccnum += 1
    return scc, sccnum

def explore(G, time, color, pred, discovered, finished, scc, sccnum, res, u):
    scc[u] = sccnum
    time = time + 1
    discovered[u] = time
    color[u] = "Gray" # indicates a back edge!
    for v in G[u]:
        if (color[v] == "White"):
            pred[v] = u
            null = explore(G, time, color, pred, discovered, finished, scc, sccnum, res, v)
    color[u] = "Black"
    time = time + 1
    finished[u] = time
    res.insert(0, u)
    return sccnum

def scc():
    G = read()
    GR = transpose(G)
    ordered = DFS_t(GR)
    scc, sccnum = DFS(G, ordered)
    return sccnum

######################################################################
def scc_paths(V, E):
    identified = set()
    stack = []
    index = {}
    boundaries = []

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        boundaries.append(index[v])

        for w in E[v]:
            if w not in index:
                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
            elif w not in identified:
                while index[w] < boundaries[-1]:
                    boundaries.pop()

        if boundaries[-1] == index[v]:
            boundaries.pop()
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in V:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc

# V - verticies, E - edges
def scc_paths2(V, E):
    identified = set()
    stack = []
    index = {}
    boundaries = []
    for v in V:
        if v not in index:
            to_do = [('VISIT', v)]
            while to_do:
                operation_type, v = to_do.pop()
                if operation_type == 'VISIT':
                    index[v] = len(stack)
                    stack.append(v)
                    boundaries.append(index[v])
                    to_do.append(('POSTVISIT', v))
                    to_do.extend(
                        reversed([('VISITEDGE', w) for w in E[v]]))
                elif operation_type == 'VISITEDGE':
                    if v not in index:
                        to_do.append(('VISIT', v))
                    elif v not in identified:
                        while index[v] < boundaries[-1]:
                            boundaries.pop()
                else:
                    if boundaries[-1] == index[v]:
                        boundaries.pop()
                        scc = set(stack[index[v]:])
                        del stack[index[v]:]
                        identified.update(scc)
                        yield scc

######################################################################
    
def launch():
    print(scc())

def launch2():
    E = read()
    V = [i for i in E]
    print(len(list(scc_paths(V, E))))
    
def launch3():
    E = read()
    V = [i for i in E]
    print(len(list(scc_paths2(V, E))))
   

############################## Launch ##############################
def usage():
    print("usage: dfs launchtype")
    print("launchtype - [plain/iter]")

if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 1):
        usage()
    else:
        if (args[0] == "plain"):
            #cProfile.run('launch()')
            launch()
        else:
            launch3()
