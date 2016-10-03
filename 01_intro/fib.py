#!/usr/bin/env python3

def fib(n):
    """Nth Fibonacci number Recursive
    Assume first number in the sequence is 0
    """
    if (n <= 1):
        return 1
    else:
        return (fib(n - 2) + fib(n - 1))


def fib_gen(n, a=0, b=1):
    """
    Fibonacci numbers generative alg
    """
    while n > 0:
        yield a
        a, b, n = b, (a + b), (n - 1)


if __name__ == '__main__':
   fibs =  [i for i in fib_gen(100)]
   
