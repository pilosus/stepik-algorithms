#!/usr/local/bin/python3

def aux_array(A):
    """Return auxiliar array where ith element contains sum of elements in A[0..i]
    """
    B = [0]
    current_sum = 0
    for i in range(len(A)):
        current_sum += A[i]
        B.append(current_sum)
    return B
        
def range_sum(B, i, j):
    """Return sum of elements in range i to j of A array.
    We assume that 0 <= i <= j < n, where n = len(A).
    We also assum that first element is 0, last is len(A) - 1"""
    #return B[j] - B[i - 1]
    return B[j + 1] - B[i]

def rsum(A, i, j):
    B = aux_array(A)
    return range_sum(B, i, j)
