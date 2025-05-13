#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    elif length == 10:
        fib_sequence = [0, 1]
        for i in range(2, length):
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)
        print(fib_sequence)