#!/usr/bin/env python3
#
import time
import math

def fibonacci_basic(n):
    if n <= 1:
        return n
    return fibonacci_basic(n-1) + fibonacci_basic(n-2)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_log(n):
    return fib_iter(1, 0, 0, 1, n)

def fib_iter(a, b, p, q, count):
    if count == 0:
        return b
    elif count % 2 == 0:
        p_prime = p**2 + q**2
        q_prime = q**2 + 2*p*q
        return fib_iter(a, b, p_prime, q_prime, count // 2)
    else:
        a_prime = b*q + a*q + a*p
        b_prime = b*p + a*q
        return fib_iter(a_prime, b_prime, p, q, count - 1)

phi = (1 + math.sqrt(5)) / 2
def fibonacci_binet(n):
    return round((phi**n - ((-phi)**-n)) / math.sqrt(5))

def time_function(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return end - start, result

n_values = [70, 71, 72, 100, 1000]

for n in n_values:
    # time_basic, result_basic = time_function(fibonacci_basic, n)
    time_memo, result_memo = time_function(fibonacci_memo, n)
    time_log, result_log = time_function(fibonacci_log, n)
    time_binet, result_binet = time_function(fibonacci_binet, n)

    print(f"n = {n}")
    # print(f"Recursion {time_basic:.6f} seconds Result:: {result_basic}")
    print(f"Memoization {time_memo:.6f} seconds Result: {result_memo}")
    print(f"Divide {time_log:.6f} seconds Result: {result_log}")
    print(f"Binet {time_binet:.6f} seconds Result: {result_binet}")
    print()
