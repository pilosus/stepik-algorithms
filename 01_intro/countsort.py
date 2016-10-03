#!/usr/local/bin/python3

n = int(input()) 
raw = input()
A = [int(x) for x in raw.split()]
M = max(A)
B = [0 for x in range(1, M + 1)]

for j in range(n):
    B[(A[j] - 1)] = B[(A[j] - 1)] + 1

k = 0
for i in range(M):
    for j in range(B[i]):
        A[k] = i + 1
        k += 1

answer = ' '.join(str(e) for e in A)
print(answer)
