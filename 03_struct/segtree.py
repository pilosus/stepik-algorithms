#!/usr/local/bin/python3

import cProfile
import sys
from math import log, floor, ceil

########## Common operations ##########
def parent(i):
    """Parent of the ith element of the seg tree"""
    return (i - 1) // 2

def left(i):
    return 2 * (i + 1) - 1

def right(i):
    return 2 * (i + 1)

def twin(S, i):
    """Return index of the element of the seg tree that is in pair with
    the element at the given index i."""
    p = parent(i)
    l = left(p)
    r = right(p)
    if (i == l):
        return r
    else:
        return l

########## Update tree ##########
def segtree_set(S, i, val):
    """Insert val to seg tree at the ith position."""
    if (i < 1):
        S[i] = val
    else:
        S[i] = val
        ### Rebuild branch up to the first element of the tree
        #### Find twin
        tw = twin(S, i)
        new_val = min(val, tw)
        par = parent(i)
        #### Insert new_val at the position of the parent
        segtree_set(S, par, new_val)

########## Find minimum on the interval ##########
def segtree_min(A, l, r):
    pass

def build_segtree(A, S):
    """Build segtree from the array of log_2 N"""
    size = len(A)
    if (size < 2):
        return S
    else:
        temp = [(min(A[i], A[i + 1])) for i in range(0, (size - 1), 2)]
        for i in range((len(temp) - 1), -1, -1):
            S.insert(0, temp[i])
        build_segtree(temp, S)


def arri2segi(A, i):
    """Return an index of segment tree corresponding to input array
    Assume that i is in range of 0 to len(A) - 1
    """
    size = len(A)
    extended_array_size = 2 ** ceil(log(size, 2))
    segtree_size = 2 * extended_array_size - 1
    return segtree_size - size + i
    

def extend_array(A):
    """Build array up to 2 ^ n"""
    size = len(A)
    extended_size = 2 ** ceil(log(size, 2))
    infinity = int(10e9) + 1
    if (extended_size > size):
        A.extend([infinity for i in range(extended_size - size)])
    ### 

def update(A, i, val):
    A[i] = val

######################################################################

INF = int(10e9) + 1

class SegmentTreeNode:
    def __init__(self, l, r, v=INF):
        self.left = l
        self.right = r
        self.value = v

    def merge(self, left, right):
        if left is not None and right is not None:
            self.value = min(left.value, right.value)
        elif left is None and right is None:
            self.value = INF
        elif left is None:
            self.value = right.value
        else:
            self.value = left.value


class SegmentTree:
    def __init__(self, a):
        n = len(a)
        power = ceil(log(n, 2)) # height of the seg tree
        total = 2 ** (power + 1) # num of nodes in the seg tree
        self.__tree = [None] * int(total)
        self.__leaf_length = int(total / 2) - 1
        self.__build(1, 0, self.__leaf_length, a)

    def __build(self, node, l, r, a):
        if l == r:
            self.__tree[node] = SegmentTreeNode(l, r)
            try:
                self.__tree[node].value = a[l]
            except IndexError:
                self.__tree[node].value = INF
            return
        leftchild = 2 * node
        rightchild = leftchild + 1
        mid = (l + r) // 2
        self.__build(leftchild, l, mid, a)
        self.__build(rightchild, mid + 1, r, a)
        self.__tree[node] = SegmentTreeNode(l, r)
        l = self.__tree[leftchild]
        r = self.__tree[rightchild]
        self.__tree[node].merge(l, r)

    def __query(self, node, l, r, i, j):
        if l >= i and r <= j:
            return self.__tree[node]
        elif j < l or i > r:
            return None
        else:
            leftchild = 2 * node
            rightchild = leftchild + 1
            mid = (l + r) // 2
            l = self.__query(leftchild, l, mid, i, j)
            r = self.__query(rightchild, mid + 1, r, i, j)
            if l is not None and r is not None:
                return SegmentTreeNode(-1, -1, min(l.value, r.value))
            elif l is None and r is None:
                return SegmentTreeNode(-1, -1, INF)
            elif l is None:
                return SegmentTreeNode(-1, -1, r.value)
            else:
                return SegmentTreeNode(-1, -1, l.value)

    def query(self, i, j): 
        return self.__query(1, 0, self.__leaf_length, i, j)

    def __update(self, node, l, r, i, v):
        if l == i and r == i:
            self.__tree[node].value = v
        elif i < l or i > r:
            return None
        else:
            leftchild = 2 * node
            rightchild = leftchild + 1
            mid = (l + r) // 2
            self.__update(leftchild, l, mid, i, v)
            self.__update(rightchild, mid + 1, r, i, v)
            l = self.__tree[leftchild]
            r = self.__tree[rightchild]
            self.__tree[node].merge(l, r)

    def update(self, i, value):
        self.__update(1, 0, self.__leaf_length, i, value)

######################################################################
def usage():
    print("usage: segtree launchtype")
    print("launchtype - [test/real]")


def segtree():
    l, nop = [int(x) for x in input().split()] # length of the array, num of operators
    A = [int(x) for x in input().split()] # Array
    ST = SegmentTree(A) # segment tree converted from the array
    while (nop > 0):
        line = input().split()
        command, arg1, arg2 = line[0], int(line[1]), int(line[2])
        if (command == 'Min'):
            print(ST.query(arg1 - 1, arg2 - 1).value)
        else:
            ST.update(arg1 - 1, arg2)
        #print("Heap: ", h) # debug
        nop -= 1

      
if __name__ == '__main__':
    args = sys.argv[1:]
    if (len(args) < 1):
        usage()
    else:
        if (args[0] == "test"):
            cProfile.run('segtree()')
        else:
            segtree()

