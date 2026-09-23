import matplotlib.pyplot as plt
import numpy as np
import time


def factorial_rekurze(n):
    if n == 0:
        return 1
    return n * factorial_rekurze(n - 1)


def factorial_iterativní(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci_rekurze(n):
    if n <= 1:
        return n
    return fibonacci_rekurze(n - 1) + fibonacci_rekurze(n - 2)


def fibonacci_iterativní(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gcd_rekurze(a, b):
    if b == 0:
        return a
    return gcd_rekurze(b, a % b)


def gcd_iterativní(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time


test_values = list(range(0, 21))
gcd_test_values = list(range(1, 100))


factorial_rekurze_cas = []
factorial_iterativní_cas = []
fibonacci_rekurze_cas = []
fibonacci_iterativní_cas = []
gcd_rekurze_cas = []
gcd_iterativní_cas = []


for n in test_values:
    factorial_rekurze_cas.append(measure_time(factorial_rekurze, n))
    factorial_iterativní_cas.append(measure_time(factorial_iterativní, n))


for n in test_values:
    fibonacci_rekurze_cas.append(measure_time(fibonacci_rekurze, n))
    fibonacci_iterativní_cas.append(measure_time(fibonacci_iterativní, n))


for n in gcd_test_values:
    gcd_rekurze_cas.append(measure_time(gcd_rekurze, n, n // 2))
    gcd_iterativní_cas.append(measure_time(gcd_iterativní, n, n // 2))


plt.figure(figsize=(8, 5))
plt.plot(test_values, factorial_rekurze_cas, label='Rekurzivní', color='r')
plt.plot(test_values, factorial_iterativní_cas, label='Iterativní', color='g')
plt.title('Čas běhu pro faktoriál')
plt.xlabel('n')
plt.ylabel('Čas (s)')
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(8, 5))
plt.plot(test_values, fibonacci_rekurze_cas, label='Rekurzivní', color='r')
plt.plot(test_values, fibonacci_iterativní_cas, label='Iterativní', color='g')
plt.title('Čas běhu pro Fibonacci')
plt.xlabel('n')
plt.ylabel('Čas (s)')
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(8, 5))
plt.plot(gcd_test_values, gcd_rekurze_cas, label='Rekurzivní', color='r')
plt.plot(gcd_test_values, gcd_iterativní_cas, label='Iterativní', color='g')
plt.title('Čas běhu pro GCD')
plt.xlabel('a, b')
plt.ylabel('Čas (s)')
plt.legend()
plt.grid()
plt.show()