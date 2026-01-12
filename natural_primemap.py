import numpy as np
import math

def is_prime(num):
    if num==2: 
        return True
    if num < 2 or not num % 2:
        return False
    for i in range(3, int(num **0.5) + 1, 2):
    # skips all evens + uptil sqrt num + 1
    # n = a.b, if a < sqrt(n), b > sqrt(n) -> proof by contradiction
        if not num%i:
            return False
    return True

def prime_map(num): # num-th prime map
    prime_map_ = {2:0}
    idx = 1 # starting index 
    for i in range(3, num+1, 2):
        if is_prime(i):
            prime_map_[i] = idx
            idx +=1
    return prime_map_
    
def primefactor_set(num, prime_map_): # returns set of primefactors for given num
    factors_ = set() # to prevent duplication

    for prime in prime_map_:
        while not num%prime:
            # while the num div prime still has a remainder of zero
            # keep dividing
            # then move to the next prime in the list 
            num//=prime
            factors_.add(prime)
        if num ==1:
            # num has been completely factored down. there are no more to be found
            # therefore, break loop 
            break
        if num in prime_map_:
            # if num is a prime, it wont satisfy above loops so it will fallback to this one
            # add it to the set 
            factors_.add(num)

    return factors_

def fill_primes(num, prime_map_, factor_array):
    # creates a 2d np array with rows as number and columns as prime number
    # entry is 1 if column val is a prime factor of row 
    for n in range(2, num):
        if n in prime_map_:
            idx = prime_map_[n]
            factor_array[n, idx] = 1
            continue
            # if n is a prime, go to corresponding index/column and set the value to 1
            # then skip factorization step w/ continue 
        factors = primefactor_set(n, prime_map_)
        for factor in factors:
            idx = prime_map_[factor]
            factor_array[n, idx] = 1
            # if n is a composite, return prime factor set and set all of those col values
            # to 1 

    return factor_array

def vectorize_map(N):
    primes = prime_map(N)
    factor_array = np.zeros((N, len(primes)), dtype='uint8') # creates an empty array with zeros 
        # init np array to have all close to zero vals $!
    factor_array = fill_primes(N, primes, factor_array) # fills in neccessary entries 
    return factor_array[1:]



# prime vs natural vector gen: use bool func to generate a map (dataset defined by fill primes function
# for n in range ... part) while bool func represents feature set -> use this map to vectorize a 2d array
# using other funcs in this case, the map was used to generate a set which was used to vectorize each
# element w/ either 0 or 1 -> generalize this process to map different datasets with feature sets  






'''
if __name__ == '__main__':
    MAX_NO = 10000
    primes_vector = vectorize_map(MAX_NO)
    print(primes_vector)
'''
     






