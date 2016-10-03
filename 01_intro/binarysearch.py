#!/usr/local/bin/python3

line1 = input()
line2 = input()
n = [int(x) for x in line1.split()][0]
A = [int(x) for x in line1.split()][1:]
k = [int(x) for x in line2.split()][0]
B = [int(x) for x in line2.split()][1:]

def binary_search(A, k):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] == k:
            return m + 1
        elif A[m] > k:
            r = m - 1
        elif A[m] < k:
            l = m + 1
    return -1

answer = ' '.join(str(e) for e in [binary_search(A, k) for k in B])
print(answer)

