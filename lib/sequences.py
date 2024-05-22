#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0 :
        print([])
        return
    fib_seq = [0, 1]

    while len(fib_seq) < length:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)

    if length == 1:
        fib_seq = [0]

    print(fib_seq[:length])

print_fibonacci(10)