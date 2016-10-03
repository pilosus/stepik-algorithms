#!/usr/local/bin/python3

import array

INF = int(10e9) + 1
p = array.array('i', [0,]*1000000) # parents indexes
rank = array.array('i', [0,]*1000000)

def makeset(x):
    p[x] = x
    rank[x] = 0

def find(x):
    if (x == p[x]):
        return x
    else:
        #p[x] = find(p[x])
        return find(p[x])

def union(x, y):
    rx = find(x)
    ry = find(y)
    if (rx == ry):
        return
    if (rank[rx] < rank[ry]):
        p[rx] = ry
    elif (rank[rx] > rank[ry]):
        p[ry] = rx
    else:
        p[ry] = rx
        rank[rx] += 1

    #if (rank[rx] > rank[ry]):
    #    p[ry] = rx
    #else:
    #    p[rx] = ry
    #    if (rank[rx] == rank[ry]):
    #        rank[ry] = rank[rx] + 1




def dsu():
    nos, noc = [int(x) for x in input().split()] # num of sets and num of commands

    #[p.append(i) for i in range(nos + 100)]
    #[rank.append(i) for i in range(nos + 100)]
    [makeset(i) for i in range(1, nos + 1)]

    while (noc > 0):
        line = input().split()
        command, arg1, arg2 = line[0], int(line[1]), int(line[2])
        if (command == 'Union'):
            union(arg1, arg2)
        else:
            #print(find(arg1 - 1) == find(arg2 - 1))
            print(find(arg1) == find(arg2))
        #print("Heap: ", h) # debug
        noc -= 1

if __name__ == '__main__':
    dsu()
