#!/usr/local/bin/python3

import sys

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


def launch():
    E = read()
    V = [i for i in E]
    print(len(list(scc_paths2(V, E))))

   
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
