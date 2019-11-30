# using "Sieve of Eratosthenes" method
import math

primes = []
composite = [False, False,]

def print_in_place(str):
    print(str,end="\r", flush=True)

def init_seive(n):
    for i in range(2, n):
        composite.append(True)

    for i in range(2, math.floor(math.sqrt(n))+1):
        if composite[i]:
            print_in_place("starting i= %s"% i)
            j=i**2
            while j < n:
                composite[j] = False
                j+=i
            print_in_place("finished i= %s" % i)


def find_primes(n):
    init_seive(n)
    i=0
    debug = 1000
    for i, is_prime in enumerate(composite):
        if is_prime:
            primes.append(i)
            i+=1
            if((i % debug)==0):
                print("prime %s found %s" % (len(primes), i), end="\r", flush=True)
    return primes
