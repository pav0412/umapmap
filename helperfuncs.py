import numpy as np
import numba as nb
from numba import jit  # use njit to make up for the inefficient code
import math


def isprime(num):  # checks if a num is prime or not
    if num == 2:
        return True
    if num < 2 or not num % 2:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        # skips all evens + uptil sqrt num + 1
        # n = a.b, if a < sqrt(n), b > sqrt(n) -> proof by contradiction
        if not num % i:
            return False
    return True


def firstkprimes(k):  # implement k square map incremental sieve later
    if k < 1:
        return np.array([])  # return empty array -> error handler for invalid input
    primes = []
    num = 2  # i love dynamic typing -> instant instantiation upon calling the var
    while len(primes) < k:
        if isprime(num):
            primes.append(num)  # super simple functional approach
        num += 1
    return np.array(
        primes
    )  # does setting np datatype actually matter ? -> set to np.int64 later


def distinctfactors(k):
    if (
        k <= 1
    ):  # should i implement this with a set later or should i use the bookmark map implementation that i plan
        # on using with the sieve implementation ? -> latter is probably the way to go
        return np.array([])  # return empty array -> error handler for invalid input
    factors = []
    while k % 2 == 0:  # check for 2 and all even factors
        if 2 not in factors:
            factors.append(2)
        k //= 2  # divide increment 2 till k isnt div by 2
    i = 3  # check for all factors. increment by 2
    while (
        i**2 <= k
    ):  # greatest factor cant be lt sqrt n -> again, proof by contradiction
        while k % i == 0:
            if i not in factors:
                factors.append(i)
            k //= i
        i += 3  # increment to next odd
        # i dont give a fuck about clean code all i care is if i understand this shit.
        # im not good enough to care about all of that yet.
    if k > 1 and k not in factors:  # factors that are missed by the above conditionals
        factors.append(k)
        # how the fuck do i toggle on and off autocomplete for lazyvim this bitch is annoying
        # when typing out comments ffs
    return np.array(factors)


# do i want to do an all factors func ? that can wait for later


def modulo(k, n):
    return k % n  # returns kmodn
    # do i need this ? ill keep it here for the time being


def hlog(k, base=math.e):
    # helper log so i dont write out math.log each time plus log div prop.
    # for faster calc? -> this is what i think but im not sure
    # would base 2 be faster ?
    return math.log(k) / math.log(base)


def divisorcount(k):
    if k <= 1:
        return 1
    count = 2  # 1 and the number itself
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            if i == k // i:  # div pairs for k are i and k//i
                count += 1  # if perfect square, only count once
            else:
                count += 2  # else count for both


def gcd(k, n):
    while n != 0:
        k, n = n, k & n  # holy shit this is so stupidly simple i love it
    return k


# YTB implemented below
# def allfactors(k): -> do i want to do an all factors func ? that can wait for later
# def eulertotient(k): -> work on this later
# def allrelativeprimes(k): -> work on this later as well.
# def alltwinprimes(k)
