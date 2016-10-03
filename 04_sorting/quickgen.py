#!/usr/local/bin/python3

import sys
from random import randint, choice

def usage():
    print("usage: quickgen N M outfile")
    print("N - number of segments")
    print("M - number of points")
    print("outfile - file name to write into")

def generate(N, M, out):
    if (N > 50000):
        N = 50000
    if (M > 50000):
        M = 50000
    f = open(out, 'w+')
    f.write(str(N) + " " + str(M) + '\n')
    for e in range(N):
        s = randint(1, 100)
        e = randint(s, 200)
        line = str(s) + " " + str(e)
        if (e != N - 1):
            line += '\n'
        f.write(line)
    f.write(" ".join(str(x) for x in [randint(1, 100) for i in range(M)]))
    f.close()
    print("File {0} successfuly generated!".format(out))

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 3):
        usage()
    else:
        N = int(args[0])
        M = int(args[1])
        out = args[2]
        generate(N, M, out)
    
