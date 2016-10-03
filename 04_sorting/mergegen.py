#!/usr/local/bin/python3

import sys
from random import randint, choice

def usage():
    print("usage: inpgen N outfile")
    print("N - number of elements in the list")
    print("outfile - file name to write into")

def generate(N, out):
    if (N >= int(10e5)):
        N = int(10e5) - 1
    f = open(out, 'w+')
    f.write(str(N) + '\n')
    for e in range(N):
        line = str(randint(1, 1000)) + " "
        f.write(line)
    f.close()
    print("File {0} successfuly generated!".format(out))

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) == 0):
        usage()
    else:
        N = int(args[0])
        out = args[1]
        generate(N, out)
    
